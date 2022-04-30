def fib(n):
    '''
    return nth fibonacci sequence number
    '''
    if n == 1 or n == 2:
        return n
    return fib(n - 1) + fib(n - 2)

a = fib

def subfix(number):
    return {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')

print(f'a(10) = {a(10)}')

for index, number in enumerate(map(fib, range(1, 10)), start=1):
    print(f'the {index}{subfix(index)} fibonacci sequence number is {number}')
