a = 1
b = 1
c = 1

def get_function():
    a = 1
    b = 1

    def function():
        c = 1
        return a, b, c
    return function
