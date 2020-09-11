# put your python code here
a = int(input())
b = int(input())
listc = []
listd = []
if a > b:
    a, b = b, a
listc.extend(range(a, b + 1))
for i in listc:
    if i % 3 == 0:
        listd.append(i)
print(sum(listd) / len(listd))
