def get_function():
    a = 1
    b = 2
    def function():
        return a, b
    return function

f = get_function()

print(f'class of f.__closure__ is {f.__closure__.__class__}')
print(f'class of get_function.__closure__ is {get_function.__closure__.__class__}')
print(f'content of f.__closure__ is {[item.__class__ for item in f.__closure__]}')
print(f'value of f.__closure__ is {[item.cell_contents for item in f.__closure__]}')
