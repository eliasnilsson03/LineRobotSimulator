# World som hanterar t.ex. is_on_line eller liknande
# 0 för svart linje
# 1 för vit linje 

import pygame


class World:
  def __init__(self, screen: pygame.Surface):
    self.screen = screen
    self.width, self.height = screen.get_size()
    
  def reflectance_at(self, x: float, y: float):
    xi = int(round(x))
    yi = self.height - 1 - int(round(y)) # Speglas (0, 0) 

    # Out of bounds
    if (xi < 0 or xi >= self.width or yi < 0 or yi >= self.height):
      return 0 # Om utanför returnera svart - tappat bort linjen

    color = self.screen.get_at(xi, yi)
    if (color == (255, 255, 255)):
      return 1
    else:
      return 0