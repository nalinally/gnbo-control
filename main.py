import http_robot_controller

ip_adresses = [
  "172.20.10.2"
]

servo_ids_list = [
  [0, 1, 2, 3]
]

servo_offsets_list = [
  [7.8, 0, 0, 0]
]

robots = []

for ip_adress, servo_ids, servo_offsets in zip(ip_adresses, servo_ids_list, servo_offsets_list):
  robots.append(http_robot_controller.HTTPRobotController(ip_adress, servo_ids, servo_offsets))


def free():
  for robot in robots:
    robot.free()