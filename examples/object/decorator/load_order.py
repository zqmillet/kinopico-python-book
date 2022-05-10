a, b, c  = 1, 1, 1

def get_function():
    b, c = 1, 1

    def function():
        c = 1
        return a, b, c, d
    return function
