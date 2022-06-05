def opposite(number):
    if number <= -1:
        return abs(number)
    else:
        return number - (number * 2)