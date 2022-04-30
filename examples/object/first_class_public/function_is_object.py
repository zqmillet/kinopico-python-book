def fib(n):
    '''
    return nth fibonacci sequence number
    '''
    if n == 1 or n == 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(f'fib(10) = {fib(10)}')
print(f'docstring of fib is {repr(fib.__doc__.strip())}')
print(f'class of fib is {fib.__class__.__name__}')
