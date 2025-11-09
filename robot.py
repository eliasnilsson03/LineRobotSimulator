import math
import pygame
from pos import Pos
import sensor

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
from sensor import Sensor
from world import World

class Robot:
    def __init__(self, x: float, y: float, theta: float, width: int, length: int, world: World):
        self.pos = Pos(x, y, theta)
        self.width = width
        self.length = length
        self.world = world
        self.speed = 80.0
        # Skapar tre sensorer alla längst fram, en placerad till vänster, en i mitten och en till höger
        # En sensor tar in värdena (x, y, angle, avstånd från mitt längdriktning, offset sidled)
        self.sensors = [
            Sensor(x, y, theta, length - 4,  width / 5),   # vänster
            Sensor(x, y, theta, length - 4,  0),           # mitten
            Sensor(x, y, theta, length - 4, -width / 5)    # höger
        ]

    def move(self, dt: float):
        # uppdaterar position
        ax = math.cos(self.pos.theta)
        ay = math.sin(self.pos.theta)
        self.pos.x += self.speed * dt * ax
        self.pos.y += self.speed * dt * ay
        # ska även uppdatera sensornas positioner

        for s in self.sensors:
            s.update(self.pos.x, self.pos.y, self.pos.theta)

    def follow_line(self, dt: float):
        for sensor in self.sensors:
            if (sensor.read(self.world) < 1):
                # self.lost_line(self)
                pass
            else:
                self.move(dt)
            

    def lost_line(self):
        pass