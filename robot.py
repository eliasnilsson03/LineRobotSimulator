class Robot:
  def __init__(self, x, y, width, height):
      self.x = x
      self.y = y
      self.width = width
      self.height = height



  def line_sensors():
      sensors = [
         (self.width / 2, -self.width / 2), # Vänster
         (self.width / 2, 0), # Mitten
         (self.width / 2, self.width / 2) # Höger
      ]

      readings = []

             
  


  # Tre sensorer, en till vänster, en i mitten och en till höger för att se pixlar
  # Om svar pixel = på linjen
  # Om vit pixle = av linjen

  # Om helt av linje, räkna hur länge sedan den gick av
  # vänd sedan i senaste riktningen