#Multi-Threading

import threading
import time

def print_hello(users):
    print("printing hello user")
    for user in users:
        time.sleep(1)
        print("Hello "+ user)
        

def print_hi(users):
    print("printing Hi users")
    for user in users:
        time.sleep(1)
        print("HI " + user)
              
        
users = ["Anju","Anu","Shanil","Bastin","Reena","Unknown"]
start_time = time.time()

#print_hello(users)
#print_hi(users)

thread1 = threading.Thread(target = print_hello, args = (users,))
thread2 = threading.Thread(target = print_hi, args = (users,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Total time= ", time.time() - start_time)
