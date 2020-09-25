# phrase ="First ladies rule the State and state the rule: ladies first"
phrase = input()
plist = phrase.split()
end_in_s = []
for i in plist:
    if i[-1] == 's':
        end_in_s.append(i)
print("_".join(end_in_s))
"""
other solutions
sentence = input().split()
s_word = [word for word in sentence if word.endswith(('s'))]
print('_'.join(s_word))

print("_".join([x for x in input().split() if x[-1] == 's']))

sentence = input().split()
s_word = [word for word in sentence if word.endswith(('s'))]
print('_'.join(s_word))
"""

