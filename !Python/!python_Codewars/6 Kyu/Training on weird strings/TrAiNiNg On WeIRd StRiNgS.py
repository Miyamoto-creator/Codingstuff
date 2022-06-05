def to_weird_case(string) :
  x_string = string.split(" ")

  solution = ""
  for word in x_string :
    for char in range(len(word)) :
      if char % 2 == 0 :
        solution += word[char].upper()
      else :
        solution += word[char].lower()
    # after each word is done, add a space

    solution += " "
  return solution.strip()


"""def to_weird_case(string):
  length = len(string)
  lst = []
  for i in range (0, length, 1):
    print(f"i is: {i}")
    if string is string.isupper() == True:
      lst.append(string[i])
    elif string is string.islower() == True:
      lst.append(string[i])
    elif string is string.isupper() == False:
      string.upper()
      lst.append(string[i])
    elif string is string.islower() == False:
      string.upper() 
      lst.append(string[i])
  return print(lst)

to_weird_case("hello")"""
