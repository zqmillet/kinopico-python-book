code = '''
a = 1
b = 1

def get_function():
    a = 1

    def function():
        b = 1
        return a, b
    return function
'''

from dis import dis
dis(code)
