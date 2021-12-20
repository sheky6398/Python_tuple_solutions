# Reverse the tuple
# Given:

# tuple1 = (10, 20, 30, 40, 50)
# Expected output:

# (50, 40, 30, 20, 10)

t = (10, 20, 30, 40, 50)
y = reversed(t)
print(tuple(y))


x = []
for i in t[::-1]:
    x.append(i)
print(tuple(x))