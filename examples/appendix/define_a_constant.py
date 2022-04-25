class _CONST:
    PI = 3.14
    E = 2.718

    def __setattr__(self, _, __):
        raise ValueError('cannot rebind constant')

CONST = _CONST()

print(f'CONST.PI = {CONST.PI}')
print(f'CONST.E = {CONST.E}')

CONST.PI = 3.15
