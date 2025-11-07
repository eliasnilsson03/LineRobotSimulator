# Vad har ett sensor objekt??
# Vi behöver: Sensorns nuvarande position 
# Hur används sensor objektet??
# I robot skapas tre olika sensorer, en för left, right och mid

# 0 för svart linje
# 1 för vit linje 

from pos import Pos
import math

class Sensor:
  def __init__(self, x: float, y: float, angle: float, d: int, s: int):
    xs = x + d * math.cos(angle) - s * math.sin(angle)
    ys = y + d * math.sin(angle) + s * math.cos(angle)

    self.pos = Pos(xs, ys, angle)


  def update(self, newX: float, newY: float, newAngle: float):
    self.pos = Pos(newX, newY, newAngle)

  def read():
    # Läs in färgen framför sensorn
    pass



# class Sensor