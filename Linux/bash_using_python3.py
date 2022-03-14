import subprocess
res=subprocess.run(['echo','hi I am Anju'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print(res.stdout)

# stderr  : it catches the error and use it later **kwargs
# text=True   : specifying output should be in string format, by default it in bytes
