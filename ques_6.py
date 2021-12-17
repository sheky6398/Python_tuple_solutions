#  Write a Python program to convert a tuple to a string.

tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
print("".join(tup))


# Another Method
res = ""
for i in tup:
    res+=i
print(res)