# Vad har ett sensor objekt??
# Vi behöver: Sensorns nuvarande position 
# Hur används sensor objektet??
# I robot skapas tre olika sensorer, en för left, right och mid

# 0 för svart linje
# 1 för vit linje 

from pos import Pos
import math

class Sensor:
  def __init__(self, x: float, y: float, angle: float, d: float, s: float):
    xs = x + d * math.cos(angle) - s * math.sin(angle)
    ys = y + d * math.sin(angle) + s * math.cos(angle)

    self.d = d
    self.s = s
    self.pos = Pos(xs, ys, angle)


  def update(self, newX: float, newY: float, newAngle: float):
    # Beräkna om x, y
    newXS = newX + self.d * math.cos(newAngle) - self.s * math.sin(newAngle)
    newYS = newY + self.d * math.sin(newAngle) + self.s * math.cos(newAngle)
    self.pos = Pos(newXS, newYS, newAngle)

  def read():
    # Läs in färgen framför sensorn
    pass



# class Sensor