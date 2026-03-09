#Date :09/03/2026

from pysimverse import Drone
import time

drone = Drone()
drone.connect()

drone.take_off()
drone.move_forward(280)
time.sleep(1)
drone.move_backward(360)
time.sleep(1)
drone.move_left(80)
time.sleep(1)
drone.move_right(80)

time.sleep(2)

drone.land()