# Write a Python program to convert a list of tuples into a dictionary.

l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
d = {}
for i,j in l:
    d.setdefault(i,[]).append(j)
print(d)