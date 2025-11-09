# Vad har ett sensor objekt??
# Vi behöver: Sensorns nuvarande position 
# Hur används sensor objektet??
# I robot skapas tre olika sensorer, en för left, right och mid

# 0 för svart linje
# 1 för vit linje 

from pos import Pos
import math
from world import World

# DÖP OM ALLA ANGLE TILL THETA
class Sensor:
  def __init__(self, x: float, y: float, theta: float, d: float, s: float):
    xs = x + d * math.cos(theta) - s * math.sin(theta)
    ys = y + d * math.sin(theta) + s * math.cos(theta)

    self.d = d
    self.s = s
    self.pos = Pos(xs, ys, theta)


  def update(self, new_x: float, new_y: float, new_theta: float):
    # Beräkna om x, y
    new_xs = new_x + self.d * math.cos(new_theta) - self.s * math.sin(new_theta)
    new_ys = new_y + self.d * math.sin(new_theta) + self.s * math.cos(new_theta)
    self.pos = Pos(new_xs, new_ys, new_theta)

  def read(self, world: World):
    x = self.pos.x
    y = self.pos.y

    value = world.reflectance_at(x, y)
    return value
    