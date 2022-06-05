first_number, second_number, operation = float(input()), float(input()), str(input())

if second_number == 0.0 and operation in ["mod", "div", "/"]:
    print("Division by 0!")
else:
    if operation == "mod" or "div" or "pow":
        first_number = str(first_number)
        second_number = str(second_number)
        if operation in "mod":
            operation = "%"
        elif operation in "div":
            operation = "//"
        elif operation in "pow":
            first_number = "(" + first_number + ")"
            operation = "**"
        print(f"{first_number} {operation} {second_number}")
        result = eval(f"{first_number} {operation} {second_number}")
        print(result)
