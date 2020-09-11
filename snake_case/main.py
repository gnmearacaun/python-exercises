aterm2 = input()
for char in aterm2:
    if char.isupper():
        aterm2 = aterm2.replace(char, "_" + char.lower())

print(aterm2)
