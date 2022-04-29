from pexpect import spawn
from sys import executable
from time import sleep

child = spawn(executable, timeout=1)
child.sendline('print(23333)\n')
print(child.before)
import pdb; pdb.set_trace()
child.sendline('exit()\n')
print(child.before)
