# Fungerar som controller
# Ritar ut robotens tillstånd på skärmen

import math
import pygame


class Renderer:
  def __init__(self, screen):
    self.screen = screen
    self.window_width, self.window_height = screen.get_size()


  def draw_sensors(self, robot):
    for sensor in robot.sensors:
        sx, sy = robot.world.world_to_pixel(sensor.pos.x, sensor.pos.y)
        
        value = sensor.read(robot.world)
        if value == 1:
            color = (255, 0, 0)           # röd = "på linje" (ljust)
        else:
            color = (0, 255, 0)           # grön = "bakgrund" (mörkt)

        pygame.draw.circle(self.screen, color, (sx, sy), 2)  

  def draw_robot(self, robot):
    robot_x, robot_y = robot.world.world_to_pixel(robot.pos.x, robot.pos.y)
    # Pygame ritar från övre vänstra hörnet
    rect_x = robot_x - robot.width // 2
    rect_y = robot_y - robot.length // 2

    pygame.draw.rect(self.screen, (201, 52, 52), (rect_x, rect_y, robot.width, robot.length))
    self.draw_sensors(robot)

  def draw_spiral(self, midx, midy):
    loops = 5 # För tätare, öka denna
    scale = 0.2 # För större spiral, öka denna
    for angle in range(0, 360 * loops, 1):
      radius = scale * angle 
      x = int(midx + radius * math.cos(math.radians(angle)))
      y = int (midy + radius * math.sin(math.radians(angle)))
      pygame.draw.circle(self.screen, (255, 255, 255), (x, y), 5)

  def draw_line(self):
    x1, y1 = 0, self.window_height // 2
    x2, y2 = self.window_width, self.window_height // 2
    # +40 respktive -40 för att inte linjen ska täcka hela fönstret
    pygame.draw.line(self.screen, (255, 255, 255), (x1 + 40, y1), (x2 - 40, y2), 10)