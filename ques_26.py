#  Write a Python program calculate the product, multiplying all the numbers of a given tuple. Go to the editor
# Original Tuple:
# (4, 3, 2, 2, -1, 18)
# Product - multiplying all the numbers of the said tuple: -864
# Original Tuple:
# (2, 4, 8, 8, 3, 2, 9)
# Product - multiplying all the numbers of the said tuple: 27648


t = (2, 4, 8, 8, 3, 2, 9)
mul = 1
for i in t:
    mul*=i
print(mul)