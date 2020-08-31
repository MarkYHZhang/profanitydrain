import wordninja

# TODO: currently using wordninja for un-spaced string tokenization
# but will eventually switch to faster and custom methods
def tokenize(untokenized_string: str) -> list:
    return wordninja.split(untokenized_string)