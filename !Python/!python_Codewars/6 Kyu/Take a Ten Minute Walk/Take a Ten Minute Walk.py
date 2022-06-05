"""You live in the city of Cartesian where all roads are laid out in a perfect grid. You arrived ten minutes too early
to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with
a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings
representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (
direction) and you know it takes you one minute to traverse one city block, so create a function that will return
true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will,
of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array (string in COBOL) containing a random assortment of direction letters (
'n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!). """

import numpy as np


def is_valid_walk(walk):
    values, counts = np.unique(walk, return_counts=True)
    walk_dict = dict(zip(values, counts))
    e_e, w_w, n_n, s_s  = walk.count('e'), walk.count('w'), walk.count('n'), walk.count('s'),
    e_w, n_s = walk.count('e') == walk.count('w'), walk.count('n') == walk.count('s')
    if sum(counts) == 10:
        if len(walk_dict) == 4:
            if n_s and e_w:
                return True
        elif len(walk_dict) == 2:
            if n_s or e_w in walk:
                return True
    return False



def is_valid_walk(walk):
    values, counts = np.unique(walk, return_counts=True)
    walk_dict = dict(zip(values, counts))
    print(len(walk_dict))
    print(walk_dict)
    print(len(walk_dict))
    e_e, w_w, n_n, s_s  = walk.count('e'), walk.count('w'), walk.count('n'), walk.count('s'),
    e_w, n_s = walk.count('e') == walk.count('w'), walk.count('n') == walk.count('s')
    print("n count: ", (walk.count('n') == walk.count('s')))
    print("e count: ", walk.count('e') == walk.count('w'))
    if sum(counts) == 10:
        print("1st if", sum(counts))
        if len(walk_dict) == 4:
            print("1 2nd if", len(walk_dict))
            if n_s and e_w:
                print("2nd 1st if", n_s)
                return print(True)
        elif len(walk_dict) == 2:
            print("1 2rd if", len(walk_dict))
            if n_s or e_w in walk:
                print("1 3rd if if", walk.count('n') == walk.count('s'))
                return print(True)
    return print(False)


is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'])
print("Should return True")
is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e'])
print("Should return False")
is_valid_walk(['w'])
print("Should return False")
is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's'])
print("Should return False")
is_valid_walk(['s', 'e', 'w', 'w', 'n', 's', 'e', 'w', 'n', 's'])
print("Should return False")
is_valid_walk(['e', 'w', 'e', 'n', 'n', 's', 'n', 's', 'e', 'w'])
print("Should return False")
is_valid_walk(['e', 'e', 'e', 'e', 'e', 'n', 'n', 'n', 'n', 'n'])
print("Should return False")
is_valid_walk(['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'])
print("Should return True")
is_valid_walk(['e', 'e', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'])
print("Should return False")

