import subprocess
process=subprocess.Popen(['ls','-la'])
process.wait()    # wait for completeing the execution of previous
print("completed")
