#  Write a Python program to compute element-wise sum of given tuples. Go to the editor
# Original lists:
# (1, 2, 3, 4)
# (3, 5, 2, 1)
# (2, 2, 3, 1)
# Element-wise sum of the said tuples:
# (6, 9, 8, 6)

t1,t2,t3 = (1, 2, 3, 4),(3, 5, 2, 1),(2, 2, 3, 1)
l = []
for i,j,k in zip(t1,t2,t3):
    l.append(i+j+k)
print(tuple(l))


#ANother Method
print(tuple((i+j+k) for i,j,k in zip(t1,t2,t3)))