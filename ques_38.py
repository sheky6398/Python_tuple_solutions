#  Check if all items in the tuple are the same
# tuple1 = (45, 45, 45, 45)
# Expected output:

# True


t = (45, 45, 45, 45)
print(all(i == 45 for i in t))