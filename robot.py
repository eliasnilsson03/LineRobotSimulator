import math
import pygame
from pos import Pos

  # Tre sensorer, en till vänster, en i mitten och en till höger för att se pixlar
  # Om vit pixel = på linjen
  # Om vit pixel = av linjen

  # Om helt av linje, räkna hur länge sedan den gick av
  # vänd sedan i senaste riktningen

# Vad gör robot??
# Skapar ett robot objekt, bestående av en rektangel med tre runda sensorer i fronten
# Använder sensor objektet för att läsa av nuvarande position och reglerar så den kan följa linjen
# Vad behöver robot innehålla??
# Pos, dvs. x, y, vinkel
# Bredd och längd
# Tre sensorer (left, right, mid)
# Vilka metoder?
# init, move, lostLine


class Robot:
  def __init__(self, x: int, y: int, angle: float, width: int, height: int, screen):
      self.pos = Pos(x, y, angle)
      self.width = width
      self.height = height
      self.screen = screen

  def move(self):
      # uppdaterar position
      self.pose.x += math.cos(self.pose.theta) * self.speed
      self.pose.y += math.sin(self.pose.theta) * self.speed
