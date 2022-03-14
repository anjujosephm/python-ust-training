import subprocess
result=subprocess.run(['cat','anju.txt'],stderr=subprocess.PIPE,text=True)
print(result.stderr)
