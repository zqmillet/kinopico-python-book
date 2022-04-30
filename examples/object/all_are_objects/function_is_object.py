def a(): pass
b = lambda: None

print(f'is function a an object? {isinstance(a, object)}')
print(f'the type of function a is {a.__class__.__name__}')
print(f'is function b an object? {isinstance(a, object)}')
print(f'the type of function b is {b.__class__.__name__}')
