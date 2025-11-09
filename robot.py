import math
import pygame
from pos import Pos
import sensor

# Tre sensorer, en till vänster, en i mitten och en till höger för att se pixlar
# Om vit pixel = på linjen
# Om svart pixel = av linjen

from sensor import Sensor
from world import World

class Robot:
    def __init__(self, x: float, y: float, theta: float, width: int, length: int, world: World):
        self.pos = Pos(x, y, theta)
        self.width = width
        self.length = length
        self.world = world
        self.speed = 40.0
        # Skapar tre sensorer alla längst fram, en placerad till vänster, en i mitten och en till höger
        # En sensor tar in värdena (x, y, theta, avstånd från mitt längdriktning, offset sidled)
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
        
        # uppdatera sensornas positioner
        for s in self.sensors:
            s.update(self.pos.x, self.pos.y, self.pos.theta)

    def follow_line(self, dt: float):
        weights = [-1, 0, 1]
        sensor_values = []
        
        for sensor in self.sensors:
            sensor_values.append(sensor.read(self.world))
        
        

        
            

    def lost_line(self):
        print("I lost the line!")
