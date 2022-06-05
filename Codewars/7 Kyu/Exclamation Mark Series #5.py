import re

def remove(s):
    return print(re.sub(r'\b!*[!]', '', s))

remove('!!!Hi !!hi!!! !hi') # '!!!Hi !!hi !hi') is expected output