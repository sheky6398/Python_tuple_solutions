# Write a Python program to remove an item from a tuple. 


tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
for i in tuplex:
    if i == 'r':
        continue
    else:
        print(i,end=",")

tup =tuplex[:2]+tuplex[3:]
print(tup)