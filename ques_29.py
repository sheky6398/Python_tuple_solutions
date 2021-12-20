# Write a Python program to convert a given tuple of positive integers into an integer. Go to the editor
# Original tuple:
# (1, 2, 3)
# Convert the said tuple of positive integers into an integer:
# 123
# Original tuple:
# (10, 20, 40, 5, 70)
# Convert the said tuple of positive integers into an integer:
# 102040570


t = (10, 20, 40, 5, 70)
print(int("".join(map(str,t))))

