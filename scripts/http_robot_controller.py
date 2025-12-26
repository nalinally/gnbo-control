import requests

class HTTPRobotController:

  servo_indexes = {"left_joint" : 0,
                   "left_extend" : 1,
                   "right_joint" : 2,
                   "right_extend" : 3}

  def __init__(self, ip_adress, servo_ids, servo_offsets):
    self.ip_adress = ip_adress
    self.prefix = f"http://{self.ip_adress}"
    self.servo_ids = servo_ids
    self.servo_offsets = servo_offsets

  def set_pos(self, index, pos):
    requests.get(f"{self.prefix}/set_pos?id={self.servo_ids[index]}&pos={pos+self.servo_offsets[index]}")

  def set_free(self, index):
    requests.get(f"{self.prefix}/set_free?id={self.servo_ids[index]}")

  def set_spd(self, index, spd):
    requests.get(f"{self.prefix}/set_spd?id={self.servo_ids[index]}&spd={spd}")

  def set_id(self, id):
    requests.get(f"{self.prefix}/set_id?id={id}")

  def get_pos(self, index):
    return float(requests.get(f"{self.prefix}/get_pos?id={self.servo_ids[index]}").content.decode())
  
  def get_spd(self, index):
    return float(requests.get(f"{self.prefix}/get_spd?id={self.servo_ids[index]}").content.decode())
  
  def get_id(self):
    return int(requests.get(f"{self.prefix}/get_id").content.decode())
  
  def index(self, name):
    return self.servo_indexes[name]
  
  def free(self):
    for id in self.servo_ids:
      self.set_free(id)