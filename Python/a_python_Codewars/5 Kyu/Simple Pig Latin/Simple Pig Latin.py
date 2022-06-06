def pig_it(text) :
    x_text = text.rsplit(" ")
    print(x_text)
    solution = []
    solution_two = []
    counter = 0
    for word in x_text:
        for char in word :
            counter += 1
            print(f"char is: {char}\n word is: {word}, {len(word)}, {len(char)}, counter: {counter}")
            if counter >= len(word) :
                counter -= len(word)
            else :
                solution.append(word[counter])
        solution_two.append(word[0] + "ay")
    solution_two.append(solution)
    print(solution_two)

    print(f"solution is: {solution}\n solution_two: {solution_two}")
    string_sol = str(solution)
    print(f"String sol is: {string_sol}")
    return print(' '.join(solution))
