# Write a Python program to convert a given list of tuples to a list of lists. Go to the editor
# Original list of tuples: [(1, 2), (2, 3), (3, 4)]
# Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
# Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
# Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]


l = [(1, 2), (2, 3), (3, 4)]
print([list(i) for i in l])

x = []
for i in l:
    x.append(list(i))
print(x)
