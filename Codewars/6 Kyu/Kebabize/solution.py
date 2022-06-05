import re
from typing import List


def kebabize(string=''):
    if not string.isnumeric():
        string = re.sub(r'[0-9]+', '', string)
        clean_string = string[len(string) - 1]
        list_indices: List[int] = []
        for i, n in enumerate(string):
            if n.upper() == n:
                list_indices.append(i)
        string = list(string)
        for i, n in enumerate(list_indices):
            string[n - 1] += "-"
        if "-" in str(string[len(string) - 1:]):
            string.pop(len(string) - 1)
            string += clean_string
        return "".join(string).lower()
    return ''

"""smart regex solution for this assignment
import re

def kebabize(s):
    return re.sub('\B([A-Z])', r'-\1', re.sub('\d', '', s)).lower()"""

print(kebabize('myCamelHas3Humps'))  # should equal my-camel-has-humps
print(kebabize('myCamelCasedString'))  # should equal 'my-camel-cased-string')
print(kebabize('SOS'))  # should equal 's-o-s')
print(kebabize('42'))  # should equal '')
print(kebabize('CodeWars'))  # should equal 'code-wars')
