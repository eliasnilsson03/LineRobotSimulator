from dataclasses import dataclass


@dataclass
class Pose:
    x: float
    y: float
    theta: float  # riktning i radianer

class Robot:
  def __init__(self, x: int, y: int, angle: float, width: int, height: int):
      self.pose = Pose(x, y, angle)
      self.x = x
      self.y = y
      self.width = width
      self.height = height

  def line_sensors(self):
      sensors = [
         (self.width / 2, -self.width / 2), # Vänster
         (self.width / 2, 0), # Mitten
         (self.width / 2, self.width / 2) # Höger
      ]

      for sensor in sensors:
         if (read(sensor) == (255, 255, 255)):
            move(self, 1, 0, 0, 0)
        

  def move(self, dx: float, dy: float, dtheta: float):
    self.pose.x += dx
    self.pose.y += dy
    self.pose.theta += dtheta 

        
  # Tre sensorer, en till vänster, en i mitten och en till höger för att se pixlar
  # Om svar pixel = på linjen
  # Om vit pixle = av linjen

  # Om helt av linje, räkna hur länge sedan den gick av
  # vänd sedan i senaste riktningen