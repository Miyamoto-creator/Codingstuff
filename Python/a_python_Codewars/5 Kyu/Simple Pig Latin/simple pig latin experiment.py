def pig_it(text) :
    x_text = text.rsplit(" ")
    print(x_text)
    solution = []
    solution_two = []
    sol_3 = []
    counter = 0
    for word in x_text :
        counter_two = 0
        counter_two += 1
        for char in word:
            counter += 1

            #print(f"word is: {word}, \n len word: {len(word)}, \ncounter: {counter}, \n{len(x_text)}\n Counter two: {counter_two}")
            if counter >= len(word) :
                counter -= len(word)
            else:
                solution.append(word[counter])
                #sol_3.append(word[counter_two])
        solution_two.append(word[0] + "ay")
        if counter >= len(x_text):
            counter -= len(x_text)
        else:
            sol_3.append(word)
    print(f"solution 3: {sol_3}")
    wtf = []
    wtf_string = ""
    for i_word in x_text:
        for h_char in i_word:
            counter += 1
            print(h_char[0], i_word, counter)
            if counter >= len(i_word):
                counter -= len(i_word)
                wtf.append(h_char)
                wtf_string += h_char
                print(wtf, wtf_string)
    print(solution)
    solution = "".join(solution)
    print(f"solution is: {solution}\n solution_two: {solution_two}")
    string_sol = str(solution)
    print(f"String sol is: {string_sol}")
    return print(''.join(solution))

pig_it("Pig latin is cool")
# expected output below
"""test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')
# solution_two.append(solution)
    # result = [None]*(len(solution)+len(solution_two))
    # result[::2] = solution
    # result[1::2] = solution_two
    # print(solution_two)"""
