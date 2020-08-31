from profanitydrain import ProfanityDrain

pd = ProfanityDrain()

delimiters_example = "so_me t-ext F---u___c++k"
print(pd.censor(delimiters_example))
# StdOut: so_me t-ext *---*___*++*

accents_example = "bîtçh thèrę"
print(pd.censor(accents_example))
# StdOut: ***** thèrę

emojis_example = "s🙃h🙃it 🙃🙃 wow"
print(pd.censor(emojis_example))
# StdOut: *🙃*🙃** 🙃🙃 wow

combined_example = "b🙃į---tch some texts F?U?č?k"
print(pd.censor(combined_example))
# StdOut: *🙃*---*** some texts *?*?*?*