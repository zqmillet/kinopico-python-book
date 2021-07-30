import sys
import platform

print('Python', sys.version)
print('OS is', platform.platform())

import subprocess
process = subprocess.Popen(['dot', '-V'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output, _ = process.communicate()

print(output.decode('utf8'))

