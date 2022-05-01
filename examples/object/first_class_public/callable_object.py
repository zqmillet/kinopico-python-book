class Add():
    def __call__(self, x, y):
        return x + y

add = Add()
print(f'add(1, 2) = {add(1, 2)}')
print(f'function add is callable? {callable(add)}')
print(f'class Add is callable? {callable(Add)}')
