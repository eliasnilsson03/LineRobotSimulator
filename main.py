import math
import pygame
from renderer import Renderer
from robot import Robot

def main():
  pygame.init()

  size = (750, 750)
  screen = pygame.display.set_mode(size)
  renderer = Renderer(screen)
  robot = Robot(0, 0, 0.0, 30, 15)
  pygame.display.set_caption("LineRobot Simulation")
  clock = pygame.time.Clock()

  running = True
  
  while running :
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      
    screen.fill((30, 30, 30))
    renderer.draw_line()
    renderer.draw_robot(robot)

    pygame.display.flip()
    clock.tick(60)

  pygame.quit()

if __name__ == "__main__":
    main()

