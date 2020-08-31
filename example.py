from cleantext import CleanText

clean_text = CleanText()

delimiters_example = "so_me t-ext F---u___c++k"
print(clean_text.clean(delimiters_example))
# StdOut: so_me t-ext *---*___*++*

accents_example = "bîtçh thèrę"
print(clean_text.clean(accents_example))
# StdOut: ***** thèrę

emojis_example = "s🙃h🙃it 🙃🙃 wow"
print(clean_text.clean(emojis_example))
# StdOut: *🙃*🙃** 🙃🙃 wow

combined_example = "b🙃į---tch some texts F?U?č?k"
print(clean_text.clean(combined_example))
# StdOut: *🙃*---*** some texts *?*?*?*