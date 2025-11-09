# 0 för svart linje
# 1 för vit linje 
import pygame

class World:
  def __init__(self, screen: pygame.Surface):
    self.screen = screen
    self.width, self.height = screen.get_size()
  
  def world_to_pixel(self, x_world: float, y_world: float):
     cx = self.width / 2
     cy = self.height / 2
     x_screen = cx + x_world
     y_screen = cy - y_world
     return int(round(x_screen)), int(round(y_screen))

  def reflectance_at(self, x_world: float, y_world: float):
    xi, yi = self.world_to_pixel(x_world, y_world)
    # Out of bounds
    if (xi < 0 or xi >= self.width or yi < 0 or yi >= self.height):
      return 0 # Om utanför returnera svart - tappat bort linjen

    color = self.screen.get_at((xi, yi))
    print(xi , yi, color)

    r, g, b = color[:3]
    brightness = (r + g + b) / 3
    if brightness > 250:
        # print("Jag returnerar 1")
        return 1
    else:
        # print(brightness)
        return 0
