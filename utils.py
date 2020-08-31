import unicodedata

def remove_accents(input_str) -> str:
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def is_ascii(string: str) -> bool:
    return len(string) == len(string.encode())