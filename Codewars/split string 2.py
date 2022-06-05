def solution(string):
    join_string = "-".join(string[i:i+2] for i in range(0, len(string), 2))
    x_string = join_string.split("-")
    underscore = "_"
    index = (len(string) - len(x_string))
    if index % 2 == 0:
      for i in range(0, index):
        print(f"1! x_num: {len(x_string)}, x_str: {x_string}, index: {index}, string: {len(string)}")
        return x_string
        break
      else:
        x_string[index] = x_string[index] + underscore
        print(f"2! x_num: {len(x_string)}, x_str: {x_string}, index: {index}, string: {len(string)}")
        return x_string
    elif index > 2:
        x_string[index] = x_string[index] + underscore
        print(f"3! x_num: {len(x_string)}, x_str: {x_string}, index: {index}, string: {len(string)}")
        return x_string
    elif index < 1:
        x_string = []
        print(f"4! x_num: {len(x_string)}, x_str: {x_string} index: {index}, string: {len(string)}")
        return x_string
