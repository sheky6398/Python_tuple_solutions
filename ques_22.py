# Write a Python program to remove an empty tuple(s) from a list of tuples. Go to the editor
# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

l = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
x = []
for i in l:
    if i != ():
        x.append(i)
print(x)
