def printer_error(string):
  x = len(string)
  denom = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"
  h = 0
  for char in string:
    if char not in denom:
      h += 1
      string.replace(char, "")
  answer = f"{h}/{x}"

  return answer
