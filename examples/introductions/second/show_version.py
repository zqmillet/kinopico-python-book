import sys
import platform

print('Python', sys.version)
print('OS is', platform.platform())

import subprocess
process = subprocess.Popen(['dot', '-V'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output, _ = process.communicate()
print(output.decode('utf8'))

process = subprocess.Popen(['gs', '-v'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output, _ = process.communicate()
print(output.decode('utf8'))

process = subprocess.Popen(['latex', '-v'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output, _ = process.communicate()
print(output.decode('utf8'))

process = subprocess.Popen(['xelatex', '-v'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output, _ = process.communicate()
print(output.decode('utf8'))

process = subprocess.Popen(['pdflatex', '-v'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output, _ = process.communicate()
print(output.decode('utf8'))

process = subprocess.Popen(['pdf2svg', '-v'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output, _ = process.communicate()
print(output.decode('utf8'))
