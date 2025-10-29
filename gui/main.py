import pygame

def main():
  pygame.init()

  screen = pygame.display.set_mode((400, 300))
  pygame.display.set_caption("LineRobot Simulation")

  running = True
  while running :
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      
      screen.fill((30, 30, 30))

      pygame.draw.circle(screen, (200, 200, 200), (200, 150), 20)

      pygame.display.flip()



  pygame.quit()


if __name__ == "__main__":
    main()