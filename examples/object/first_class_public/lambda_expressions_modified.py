def _(x, y):
    return x + y
add = _
print(f'1 + 2 = {add(1, 2)}')

def _(x):
    return x[-1]
names = sorted(['qiqi', 'haha', 'popo'], key=_)
print(names)
