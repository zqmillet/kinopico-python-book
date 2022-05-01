def add(x, y):
    return x + y

sub = lambda x, y: x - y

print(f'add.__call__ is {add.__call__}')
print(f'add(1, 2) = {add(1, 2)}')
print(f'add.__call__(1, 2) = {add.__call__(1, 2)}')
print()
print(f'sub.__call__ is {sub.__call__}')
print(f'sub(1, 2) = {sub(1, 2)}')
print(f'sub.__call__(1, 2) = {sub.__call__(1, 2)}')
