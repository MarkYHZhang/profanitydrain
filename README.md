# ProfanityDrain

ProfanityDrain is a python text filteration library that is able to handle many tricky scenarios where traditional textual profanity filters fail.

This includes:
* Adding abnormal delimiters between texts. e.g. "h_e_llo the--r-e"
* Using accented letters. e.g. "Càn yôū śee mę?"
* Mixed in emojis. e.g. "L👏🏼i👏🏼k👏🏼e T👏🏼h👏🏼i👏🏼s"
* more!

By default it performs selective filtering, where, only parts of the input that should be censored is censored while keeping all other parts of the text in its original form.

It is understood that efficiency is crucial for text filteration system, as of yet, ProfanityDrain has a complexity that is upper bounded by O(10n) where n is the length of the input string. It is within plans to actively reduce its complexity.

## Example usage
![Example usage](https://github.com/MarkYHZhang/profanitydrain/blob/master/readme/example.png "Example usage")

## TODOs
- [ ] Custom word splitter (improved accuracy and efficiency)
- [ ] Publish pip package
- [ ] Custom censor dictionary support
- [ ] Character substitution support
