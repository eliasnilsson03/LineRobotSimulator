import math
import pygame
from robot import Robot


def drawRobot(robot, screen):
 pygame.draw.rect(screen, (201, 52, 52), (robot.pos.x, robot.pos.y, robot.width, robot.height))

def draw_line(screen, midx, midy):
  loops = 5 # För tätare, öka denna
  scale = 0.2 # För större spiral, öka denna
  for angle in range(0, 360 * loops, 1):
    radius = scale * angle 
    x = int(midx + radius * math.cos(math.radians(angle)))
    y = int (midy + radius * math.sin(math.radians(angle)))
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 5)


def main():
  pygame.init()

  size = (750, 750)
  screen = pygame.display.set_mode(size)
  robot = Robot(350, 350, 0.0, 30, 15, screen)
  pygame.display.set_caption("LineRobot Simulation")
  clock = pygame.time.Clock()

  running = True
  
  while running :

    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      
    dt = clock.get_time() / 1000.0
    screen.fill((30, 30, 30))
    draw_line(screen, size[0] / 2, size[1] / 2)
    drawRobot(robot, screen)


    pygame.display.flip()
    clock.tick(60)


  pygame.quit()

if __name__ == "__main__":
    main()

