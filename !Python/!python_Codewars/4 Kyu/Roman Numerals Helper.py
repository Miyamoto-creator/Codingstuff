roman = {'M': 1000,
         'CM': 900,
         'D': 500,
         'CD': 400,
         'C': 100,
         'XC': 90,
         'L': 50,
         'XL': 40,
         'X': 10,
         'IX': 9,
         'V': 5,
         'IV': 4,
         'I': 1}


class RomanNumerals:
    def to_roman(num):
        string = []
        while num > 0:
            for i, j in enumerate(roman.items()):
                if num == 0:
                    break
                elif num >= j[1]:
                    string.append(j[0])
                    num -= j[1]
                    break
        return "".join(string)

    def from_roman(s):
        i, num = 0, 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i + 2] in roman:
                num += roman[s[i:i + 2]]
                i += 2
            else:
                num += roman[s[i]]
                i += 1
        return num


R = RomanNumerals

#print(R.from_roman('IV'))
#print("IV should return 4")
# print(R.from_roman('XXI'))
# print("XXI should return 21")
#print(R.test_roman(610))
#print("This is test roman, should be CDX")
print(f"{R.to_roman(1990)} should equal MCMXC")
print(f"{R.to_roman(1998)} should equal MCMXCVIII")
print(f"{R.to_roman(1666)} should equal MDCLXVI")
print(f"{R.to_roman(2008)} should equal MMVIII")
print(f"{R.to_roman(610)} should equal DCX")
print(f"{R.to_roman(2009)} should equal MMIX are they equal?")
print(f"{R.to_roman(917)} should equal CMXVII are they equal?")
print(f"{R.to_roman(2779)} should equal MMDCCLXXIX are they equal?")

# print(R.to_roman(1000))
# print("1000 should return M")
# print(R.to_roman(1666))
# print("1666 should return MDCLXVI")
# print(R.to_roman(1990))
# print("1990 Should return MCMXC")


# def test_roman(val):
#     chunks = []
#     name = ""
#     for i, char in enumerate(roman.items()):
#         qty = val // char[1]
#         if qty:
#             chunks.append(char[0] * qty)
#         val = val % char[1]
#     return "".join(chunks)

# if len(j[0]) == 1 else '#' + j[0] + '#'