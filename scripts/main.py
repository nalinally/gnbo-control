from http_robot_driver import HTTPRobotDriver
from http_robot_operator import HTTPRobotOperator
import time
import threading

ip_adresses = [
  "172.20.10.4",
  "172.20.10.2",
]

servo_ids_list = [
  [0, 1, 2, 3],
  [0, 1, 2, 3],
]

servo_offsets_list = [
  [7.8, 0, 0, 0],
  [-9, 0, 0, 0],
]

servo_reverses = [
  [True, False]
]

names = [
  "0",
  "1"
]

drivers = []
operators = []

for ip_adress, servo_ids, servo_offsets, servo_reverse, name in zip(ip_adresses, servo_ids_list, servo_offsets_list, servo_reverses, names):
  drivers.append(HTTPRobotDriver(ip_adress, servo_ids, servo_offsets, servo_reverse))
  operators.append(HTTPRobotOperator(drivers[-1], time.time, f"operator{name}"))

def main():
  thread = threading.Thread(target=main_loop)
  thread.start()

def standby():
  for driver in [drivers[0]]:
    driver.rotate(0, 90)
    # time.sleep(3.0)
    driver.rotate(1, -90)

def main_loop():
  while True:
    update()
    time.sleep(0.001)

def update():
  for operator in operators:
    operator.update()

def free():
  for driver in drivers:
    driver.free()

if __name__=="__main__":
  main()
