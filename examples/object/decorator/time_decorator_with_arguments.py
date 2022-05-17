from time import time
from functools import wraps

def print_time(message):
    def wrapper(function):
        @wraps(function)
        def _print_time(*args, **kwargs):
            now = time()
            return_value = function(*args, **kwargs)
            print(message % (time() - now))
            return return_value
        return _print_time
    return wrapper 

@print_time(message='consuming time %fs')
def add(x, y):
    return x + y

print(f'add(1, 2) = {add(1, 2)}')
print(f'add(3, 2) = {add(3, 2)}')
