import math
import pygame
from renderer import Renderer
from robot import Robot
from world import World

def main():
  pygame.init()

  size = (750, 750)
  screen = pygame.display.set_mode(size)  
  renderer = Renderer(screen)
  world = World(screen)
  robot = Robot(0, 0, 0.0, 50, 25, world)
  pygame.display.set_caption("LineRobot Simulation")
  clock = pygame.time.Clock()

  running = True
  
  while running :
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False


    screen.fill((30, 30, 30))
    renderer.draw_line()

    dt = clock.tick(60) / 1000.0
    robot.follow_line(dt)

    renderer.draw_robot(robot)
    
    pygame.display.flip()

  pygame.quit()

if __name__ == "__main__":
    main()

