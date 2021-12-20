# Write a Python program to convert a tuple to a dictionary.

tuplex = ((2, "w"),(3, "r"))
print(dict(tuplex))

#Another method
print(dict((y,x) for x,y in tuplex))

#Another Method
d = {}
for i,j in tuplex:
    d[j]=i
print(d)