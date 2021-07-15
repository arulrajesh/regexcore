from regex_core import RegexCore
rege = RegexCore()
pattern = ['''"test* exit"''','''[word1 word2]''']
for patt in pattern:
    print (f'{patt} : {rege.compose(patt, limit=30)}')