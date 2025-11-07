# Fungerar som controller
# Ritar ut robotens tillstånd på skärmen

import math
import pygame


class Renderer:
  def __init__(self, screen):
    self.screen = screen
    self.window_width, self.window_height = screen.get_size()

  def world_to_screen(self, x_world, y_world):
    cx = self.window_width / 2
    cy = self.window_height / 2
    x_screen = cx + x_world
    y_screen = cy - y_world
    return x_screen, y_screen

  # def draw_sensors(self, robot):
  #   for sensor in robot.sensors:
  #       sx, sy = self.world_to_screen(sensor.pos.x, sensor.pos.y)

  #       value = sensor.read(robot.world)
  #       if value == 1:
  #           color = (255, 0, 0)           # röd = "på linje" (ljust)
  #       else:
  #           color = (0, 255, 0)           # grön = "bakgrund" (mörkt)

  #       pygame.draw.circle(self.screen, color, (sx, sy), 4)  

  def draw_robot(self, robot):
    robot_x, robot_y = self.world_to_screen(robot.pos.x, robot.pos.y)
    # Pygame ritar från övre vänstra hörnet
    rect_x = robot_x - robot.width // 2
    rect_y = robot_y - robot.length // 2

    pygame.draw.rect(self.screen, (201, 52, 52), (rect_x, rect_y, robot.width, robot.length))

    tip_len = 20
    tip_x = robot.pos.x + tip_len * math.cos(robot.pos.theta)
    tip_y = robot.pos.y + tip_len * math.sin(robot.pos.theta)
    tx, ty = self.world_to_screen(tip_x, tip_y)
    pygame.draw.line(self.screen, (0, 0, 0), (robot_x, robot_y), (tx, ty), 2)

    # self.draw_sensors(robot)

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
    pygame.draw.line(self.screen, (255, 255, 255), (x1, y1), (x2, y2), 1)