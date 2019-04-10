import random
from config import *


class AvailableCase:

    """class that check if case is available to display randomly generated items"""
    
    def __init__(self, attribute_picture, maze):
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.maze = maze
        self.load = True
        self.attribute_picture = attribute_picture

    def display(self, attribute_picture, screen):
        while self.load:
            self.case_x = random.randint(0, 14)  
            self.case_y = random.randint(0, 14)  
            if self.maze.laby[self.case_y][self.case_x] == path: 
                self.y = self.case_y * sprite_size
                self.x = self.case_x * sprite_size
                self.load = False

