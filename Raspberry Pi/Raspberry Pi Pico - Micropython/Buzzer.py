from machine import Pin
import utime


led2=Pin(14,Pin.OUT)
buzz=Pin(15,Pin.OUT)

while True:
   
    led2.toggle()
    utime.sleep(0.5)
