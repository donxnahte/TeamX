#Date :09/03/2026

from pysimverse import Drone
import time

drone = Drone()
drone.connect()

drone.take_off(100)
drone.move_forward(250)
drone.move_right(250)

drone.land()