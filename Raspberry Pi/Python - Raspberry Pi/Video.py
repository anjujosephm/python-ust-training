from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(2)
camera.start_recording('/home/pi/Desktop/abc.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()
