text = "test"

def rot13(s):
    rot13 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
    return s.translate(rot13)


print(rot13(text))


# def rot13(s):
#     chars = "abcdefghijklmnopqrstuvwxyz"
#     trans = chars[13:]+chars[:13]
#     rot_char = lambda c: trans[chars.find(c)] if chars.find(c)>-1 else c
#     return ''.join( rot_char(c) for c in s )
