# Write a Python program to convert a tuple of string values to a tuple of integer values. Go to the editor
# Original tuple values:
# (('333', '33'), ('1416', '55'))
# New tuple values:
# ((333, 33), (1416, 55))

t = (('333', '33'), ('1416', '55'))
print(tuple((int(i[0]),int(i[1])) for i in t))
