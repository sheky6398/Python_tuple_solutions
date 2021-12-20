# Write a Python program to sort a tuple by its float element. Go to the editor
# Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]

l = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
x = []
for i in sorted(l,reverse = True):
    x.append(i)
print(x)