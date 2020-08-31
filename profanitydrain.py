from io import StringIO
from collections import deque

import tokenizer
import utils

class ProfanityDrain:

    DEFAULT_CENSORED: set = {
        "fuck",
        "bitch",
        "shit",
    }

    CENSOR_CHAR = '*'

    DELIMITERS = {
        " ", "~", "`", "!", "@", "#", "$", "+", "^", "&", "*", ".", ",", "?", "_"
    }

    
    def __init__(self, censored_set: set=DEFAULT_CENSORED, censor_file_path: str=None):
        self.censored_set = censored_set
        if censor_file_path is not None:
            try:
                self.censor_file = open(censor_file_path, "r")
            except FileNotFoundError:
                raise ValueError("Invalid file path: ", censor_file_path)
    

    def __delimiter_filter(self, text: str) -> (str, dict):
        delimiter_locs = {}
        result_text_buffer = StringIO()
        for i, c in enumerate(text):
            if c in self.DELIMITERS:
                delimiter_locs[i] = c
            else:
                result_text_buffer.write(c)
        return result_text_buffer.getvalue(), delimiter_locs
    

    def __accent_filter(self, text: str) -> (str, dict):
        normalized = utils.remove_accents(text)
        accent_locs = {}
        for i, c in enumerate(text):
            if c != normalized[i]:
                accent_locs[i] = c
        return normalized, accent_locs


    def __non_alpha_filter(self, text: str) -> (str, dict):
        non_ascii_locs = {}
        result_text_buffer = StringIO()
        for i, c in enumerate(text):
            if not utils.is_ascii(c) or not c.isalpha():
                non_ascii_locs[i] = c
            else:
                result_text_buffer.write(c)
        return result_text_buffer.getvalue(), non_ascii_locs


    def __is_censored(self, text: str) -> bool:
        return text.lower() in self.censored_set


    def __defilter(self, length: int, in_deque: deque, filter_dict: dict, replace=False):
        ptr = 0
        while ptr < length:
            if ptr in filter_dict:
                if replace:
                    if (in_deque[ptr] != self.CENSOR_CHAR):
                        in_deque[ptr] = filter_dict[ptr]
                else:
                    in_deque.insert(ptr, filter_dict[ptr])
            ptr += 1


    def censor(self, text: str) -> str:
        # restoration order must be reverse of the order below
        no_delimiters_text, delimiters = self.__delimiter_filter(text)
        normalized_text, accents = self.__accent_filter(no_delimiters_text)
        alpha_text, non_asciis = self.__non_alpha_filter(normalized_text)
        
        words: list = tokenizer.tokenize(alpha_text)
        word_ptr: int = 0
        while word_ptr < len(words):
            word: str = words[word_ptr]
            if self.__is_censored(word):
                words[word_ptr] = self.CENSOR_CHAR * len(word)
            word_ptr += 1

        censored_deque: deque = deque("".join(words))
        self.__defilter(len(normalized_text), censored_deque, non_asciis)
        self.__defilter(len(no_delimiters_text), censored_deque, accents, True)
        self.__defilter(len(text), censored_deque, delimiters)

        return "".join(list(censored_deque))
