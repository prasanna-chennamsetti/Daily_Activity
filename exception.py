try:
    c=12/0
    print("Divided")
except ZeroDivisionError:
    print("Divisible by zero error")
except TypeError:
    print("Type mismatch")