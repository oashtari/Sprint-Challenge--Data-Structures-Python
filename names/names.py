import time
from bst import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# ORIGINAL CODE

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# FASTER SOLUTION, but I need to use a data structure :facepalm:, almost did not see that
# for name_1 in names_1:
#     if name_1 in names_2:
#         print('name', name_1)
#         duplicates.append(name_1)

# BST solution
new_tree = BinarySearchTree(names_1[0])

for name in range(1, len(names_1)):
    new_tree.insert(names_1[name])

for name in names_2:
    if new_tree.contains(name):
        duplicates.append(name)

# could not figure out how to compare to BSTs :(


# other_tree = BinarySearchTree(names_2[0])

# for name in range(1, len(names_2)):
#     other_tree.insert(names_2[name])



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
