import re, pyperclip
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
)''', re.VERBOSE)
text = str(pyperclip.paste())
matches = []
for groups in email_regex.findall(text):
    matches.append(groups[0])

if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('クリップボードにコピーしました：')
    print('\n'.join(matches))
else:
    print('ねーよばーか')