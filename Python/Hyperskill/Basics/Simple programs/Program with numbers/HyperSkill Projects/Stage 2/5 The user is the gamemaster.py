# write your code here
selection = input("Enter cells: ")

print("---------")
my_string = """| {0} {1} {2} |
| {3} {4} {5} |
| {6} {7} {8} |
"""
print(my_string.format(selection[0], selection[1], selection[2], selection[3], selection[4], selection[5],
                       selection[6], selection[7], selection[8]))
print("---------")
