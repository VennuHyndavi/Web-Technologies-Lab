a = input("enter a sentence").split()
d = {}
for i in a:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i]=1
print(d.items())
