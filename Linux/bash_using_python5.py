# communicate()    : it is used to output and error, also used to write input to indicate to the subprocess

import subprocess
from sys import stdout
process=subprocess.Popen(['echo','welcome to ust'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result=process.communicate()
print(result)
