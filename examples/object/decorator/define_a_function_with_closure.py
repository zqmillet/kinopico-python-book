def get_function():
    a = 1
    def function():
        return a
    return function

b = get_function()()
pass
