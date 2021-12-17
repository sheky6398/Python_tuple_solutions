# Write a Python program to get the 4th element and 4th element from last of a tuple. 

tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
for i,j in enumerate(tuplex):
    if i ==4:
        print(j)


# ANother Method
item =  tuplex[-4]
print(item)