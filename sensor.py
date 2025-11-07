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
  def __init__(self, x: float, y: float, angle: float, d: float, s: float):
    xs = x + d * math.cos(angle) - s * math.sin(angle)
    ys = y + d * math.sin(angle) + s * math.cos(angle)

    self.d = d
    self.s = s
    self.pos = Pos(xs, ys, angle)


  def update(self, new_x: float, new_y: float, new_angle: float):
    # Beräkna om x, y
    new_xs = new_x + self.d * math.cos(new_angle) - self.s * math.sin(new_angle)
    new_ys = new_y + self.d * math.sin(new_angle) + self.s * math.cos(new_angle)
    self.pos = Pos(new_xs, new_ys, new_angle)

  def read(self, world: World):
    x = self.pos.x
    y = self.pos.y

    value = world.reflectance_at(x, y)
    return value
    