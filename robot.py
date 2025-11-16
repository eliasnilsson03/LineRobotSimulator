from enum import Enum
import math
import pygame
from PID import PID
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
        self.PID = PID(0.8, 0.0, 0.05, 0)
        
        self.last_pv = 0
        self.last_u = 0
        self.last_on_line_pos = Pos(0, 0, 0)
        
        # Skapar tre sensorer alla längst fram, en placerad till vänster, en i mitten och en till höger
        # En sensor tar in värdena (x, y, theta, avstånd från mitt längdriktning, offset sidled)
        self.sensors = [
            Sensor(x, y, theta, length - 4,  width / 5),   # vänster
            Sensor(x, y, theta, length - 4,  0),           # mitten
            Sensor(x, y, theta, length - 4, -width / 5)    # höger
        ]
 
    def move(self, dt: float, u: float):
        v_left = self.speed - u
        v_right = self.speed + u

        v_new = (v_left + v_right) / 2
        omega = (v_right - v_left) / self.width
        self.pos.theta += omega


        ax = math.cos(self.pos.theta)
        ay = math.sin(self.pos.theta)
        self.pos.x += v_new * dt * ax
        self.pos.y += v_new * dt * ay
        
        self.last_on_line_pos = Pos(self.pos.x, self.pos.y, self.pos.theta)

        # uppdatera sensornas positioner
        for s in self.sensors:
            s.update(self.pos.x, self.pos.y, self.pos.theta)

    def follow_line(self, dt: float):
        
        sensor_offsets = []
        sensor_values = []

        for sensor in self.sensors:
            sensor_offsets.append(sensor.get_offset())
            sensor_values.append(sensor.read(self.world))

        sum_sensor_values = sum(sensor_values)
        
        if (sum_sensor_values == 0):
            self.PID.reset()
            self.lost_line(dt)
        else: 
            pv = sum(s * value for s, value in zip(sensor_offsets, sensor_values)) / sum_sensor_values
            u = self.PID.compute(pv, dt)
            self.last_pv = pv
            self.last_u = u
            self.move(dt, u)
         
    def lost_line(self, dt):
        print("I lost the line!")

        # uppdatera sensornas positioner
        for s in self.sensors:
            s.update(self.pos.x, self.pos.y, self.pos.theta)
        
