def disemvowel(string_) :
    vowels = "a", "i", "e", "o", "u"
    for x in string_.lower() :
        if x in vowels :
            return string_.replace(x, "")

