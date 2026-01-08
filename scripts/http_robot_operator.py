from http_robot_driver import HTTPRobotDriver

class HTTPRobotOperator():

  def __init__(self, driver, t):
    self.driver = driver
    self.t = t
    self.extendings = [False, False]
    self.extend_vels = [0, 0]
    self.extend_end_times = [0, 0]
    self.rotatings = [False, False]
    self.rotate_poses = [0, 0]
    self.rotate_end_times = [0, 0]

  def rotate_target_pos(t):
    return

  def extend(self, leftright, vel, duration = 3.0):
    self.extendings[leftright] = True
    self.extend_vels[leftright] = vel
    self.extend_end_times[leftright] = self.t() + duration

  def rotate(self, leftright, pos, duration = 3.0):
    self.rotatings[leftright] = True
    self.rotate_poses[leftright] = pos
    self.rotate_end_times[leftright] = self.t() + duration
    start_pos = self.driver.rotate_pos[leftright]
    start_time = self.t()
    def target_pos(t):
      return start_pos + (pos - start_pos) * (t - start_time) / duration
    self.rotate_target_pos = target_pos

  def update(self):
    for leftright in [0, 1]:
      if self.extendings[leftright]:
        if self.t() >= self.extend_end_times[leftright]:
          self.driver.extend(leftright, 0)
          self.extendings[leftright] = False
        else:
          self.driver.extend(leftright, self.extend_vels[leftright])

      if self.rotatings[leftright]:
        if self.t() >= self.rotate_end_times[leftright]:
          self.rotatings[leftright] = False
        else:
          self.driver.rotate(leftright, self.rotate_target_pos(self.t()))
      



  