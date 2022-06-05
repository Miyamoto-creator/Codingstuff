import codecs

def rot13(message):
    return codecs.encode(message, 'rot_13')

# https://www.codewars.com/kata/52223df9e8f98c7aa7000062/solutions/python