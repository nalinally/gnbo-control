from http_robot_driver import HTTPRobotDriver
from http_robot_operator import HTTPRobotOperator
import time
import threading
import numpy as np

ip_adresses = [
  "172.20.10.5",
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
  True, False
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

def walk():
  start = time.time()
  phi = np.deg2rad(90)
  omega = 3
  A = 10
  while True:
    t = time.time() - start
    angles = [[90 + A * np.cos(omega * t), -90 - A * np.cos(omega * t)], 
              [90 + A * np.cos(omega * t + phi), -90 - A * np.cos(omega * t + phi)]]
    rotate(angles)

def cycle():
  standby()
  time.sleep(0.5)
  operator_row = [operators[0], operators[1], operators[2]]
  while True:
    one_cycle(operator_row)

def one_cycle(operator_row):
  t_1 = 1.0  # make triangle
  operator_row[-1].rotate(0, 30, t_1)
  operator_row[-1].rotate(1, -30, t_1)
  operator_row[-2].rotate(1, 30, t_1)
  operator_row[-3].rotate(0, -30, t_1)
  time.sleep(t_1)
  t_2 = 1.0  # 
  operator_row[-1].extend(0, -10, t_2)
  operator_row[-2].extend(1, -10, t_2)
  time.sleep(t_2)
  t_3 = 1.0
  operator_row[-1].rotate(1, -90, t_3)
  operator_row[-1].rotate(0, 90, t_3)
  operator_row[-2].rotate(0, 1, -90, t_3)
  operator_row[-3].rotate(0, 90, t_3)
  time.sleep(t_3)
  operator_row[-1].extend(0, 10, t_2)
  operator_row[-2].extend(1, 10, t_2)
  time.sleep(t_2)
  operator_row.inssert(0, operator_row.pop(-1))

def rotate(poses):
  for i in range(len(poses)):
    drivers[i].rotate(0, poses[i][0])
    drivers[i].rotate(1, poses[i][1])

def rotate_all(pos):
  for driver in drivers:
    driver.rotate(0, pos[0])
    driver.rotate(1, pos[1])

def standby():
  rotate_all([90, -90])

def init():
  rotate_all([135, -135])

def free():
  for driver in drivers:
    driver.free()

def main_loop():
  while True:
    update()
    time.sleep(0.001)

def update():
  for operator in operators:
    operator.update()

if __name__=="__main__":
  main()
