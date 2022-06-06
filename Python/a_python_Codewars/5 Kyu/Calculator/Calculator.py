def expr(number, operation = None):
    if operation == None:
        return number
    else:
        return operation(number)

def zero(Operation = None): return expr(0, Operation)
def one(Operation = None): return expr(1, Operation)
def two(Operation = None): return expr(2, Operation)
def three(Operation = None): return expr(3, Operation)
def four(Operation = None): return expr(4, Operation)
def five(Operation = None): return expr(5, Operation)
def six(Operation = None): return expr(6, Operation)
def seven(Operation = None): return expr(7, Operation)
def eight(Operation = None): return expr(8, Operation)
def nine(Operation = None): return expr(9, Operation)

def plus(a): return lambda b: b + a
def minus(a): return lambda b: b - a
def times(a): return lambda b: b * a
def divided_by(a): return lambda b: b / a