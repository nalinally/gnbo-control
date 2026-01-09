import requests
import numpy as np

class HTTPRobotDriver():

  servo_indexes = {"left_rotate" : 0,
                   "left_extend" : 1,
                   "right_rotate" : 2,
                   "right_extend" : 3}
  
  rotate_limits = [-120, 120]

  arm_clearance = 45

  def __init__(self, ip_adress, servo_ids, servo_offsets, servo_reverse):
    self.ip_adress = ip_adress
    self.prefix = f"http://{self.ip_adress}"
    self.servo_ids = servo_ids
    self.servo_offsets = servo_offsets
    self.servo_reverse = servo_reverse

    self.rotate_pos = [HTTPRobotDriver.rotate_limits[1], HTTPRobotDriver.rotate_limits[0]]

  def set_pos(self, index, pos):
    print(requests.get(f"{self.prefix}/set_pos?id={self.servo_ids[index]}&pos={pos}").content.decode())

  def set_free(self, index):
    print(requests.get(f"{self.prefix}/set_free?id={self.servo_ids[index]}").content.decode())

  def set_spd(self, index, spd):
    return requests.get(f"{self.prefix}/set_spd?id={self.servo_ids[index]}&spd={spd}").content.decode()

  def set_id(self, id):
    return requests.get(f"{self.prefix}/set_id?id={id}").content.decode()

  def get_pos(self, index):
    return float(requests.get(f"{self.prefix}/get_pos?id={self.servo_ids[index]}").content.decode())
  
  def get_spd(self, index):
    return float(requests.get(f"{self.prefix}/get_spd?id={self.servo_ids[index]}").content.decode())
  
  def get_id(self):
    return int(requests.get(f"{self.prefix}/get_id").content.decode())
  
  def rotate(self, leftright, pos_):
    index = self.index("left_rotate") if leftright == 0 else self.index("right_rotate")
    range = self.rotate_range(leftright)
    pos = np.clip([pos_], range[0] , range[1])[0]
    pos = pos * (1 if leftright == 0 else -1) * (-1 if self.servo_reverse else 1)
    self.rotate_pos[leftright] = pos_
    self.set_pos(index, pos + self.servo_offsets[index])

  def extend(self, leftright, vel):
    index = self.index("left_extend") if leftright == 0 else self.index("right_extend")
    self.set_pos(index, vel)

  def rotate_range(self, leftright):
    if leftright == 0:
      return [np.max([HTTPRobotDriver.rotate_limits[0], self.rotate_pos[1]]), HTTPRobotDriver.rotate_limits[1]]
    else:
      return [HTTPRobotDriver.rotate_limits[0], np.min([HTTPRobotDriver.rotate_limits[1], self.rotate_pos[0]])]

  def index(self, name):
    return HTTPRobotDriver.servo_indexes[name]
  
  def free(self):
    for id in self.servo_ids:
      self.set_free(id)

  def free_rotate(self):
    self.set_free(self.index("left_rotate"))
    self.set_free(self.index("right_rotate"))

  def free_extend(self):
    self.set_free(self.index("left_extend"))
    self.set_free(self.index("right_extend"))