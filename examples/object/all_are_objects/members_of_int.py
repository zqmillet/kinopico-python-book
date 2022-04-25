a = 1

print(f'there are {len(a.__dir__())} members of int')
print(f'they are {", ".join(a.__dir__())}')
print(f'the class of {repr(a)} is {a.__class__.__name__}')
