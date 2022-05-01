def add(x, y):
    return x + y

sub = lambda x, y: x - y

add.__call__ = sub.__call__

print(f'add.__call__ is {add.__call__}')
print(f'sub.__call__ is {sub.__call__}')
print(f'add(1, 2) = {add(1, 2)}')
print(f'add.__call__(1, 2) = {add.__call__(1, 2)}')
