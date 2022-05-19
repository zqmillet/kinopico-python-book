from time import time
from functools import wraps

class print_time:
    def __init__(self, message):
        self.message = message

    def __call__(self, function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            now = time()
            return_value = function(*args, **kwargs)
            print(self.message % (time() - now))
            return return_value
        return wrapper

@print_time(message='consuming time %fs')
def add(x, y):
    return x + y

print(f'add(1, 2) = {add(1, 2)}')
print(f'add(3, 2) = {add(3, 2)}')
