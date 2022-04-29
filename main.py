from pexpect import spawn
from sys import executable

code = '''
a = 1000
b = 1000
print(a is b)
for i in range(10):
    print(i)

exit()
'''

child = spawn(executable)
for line in code.strip().splitlines():
    child.sendline(line)
print(child.read().decode().replace('\r', '').replace(code, '\n').strip())
