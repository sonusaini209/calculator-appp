
# calc_function.py

def do_addition(a,b):
    return a+b

def do_substraction(a,b):
    return a-b

def do_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = "invalid result"
    return result
