import pygame
from config import *
from pygame.locals import *


class Mcgiver:
    
    """ Main character class """
    
    def __init__(self, right, left, up, down, maze):
        
        """ Setting sprites for each directions """
        
        self.right = pygame.image.load(right_giver_sprite).convert_alpha()
        self.left = pygame.image.load(left_giver_sprite).convert_alpha()
        self.down = pygame.image.load(down_giver_sprite).convert_alpha()
        self.up = pygame.image.load(up_giver_sprite).convert_alpha()

        """ Main character's initial location """
        
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0

        """ Charater default sprite and level """
        
        self.direction = self.down
        self.maze = maze

    def move(self, direction):
        
        """ Defining movement

            For each directions, we check if the next \
            tile is not a wall or is located outside the screen
            
        """

        if direction == mv_right:
            if self.case_x < (sprite_side - 1):
                if self.maze.laby[self.case_y][self.case_x + 1] != wall:
                    self.case_x += 1
                    self.x = self.case_x * sprite_size
            self.direction = self.right

        if direction == mv_left:
            if self.case_x > 0:
                if self.maze.laby[self.case_y][self.case_x - 1] != wall:
                    self.case_x -= 1
                    self.x = self.case_x * sprite_size
            self.direction = self.left

        if direction == mv_up:
            if self.case_y > 0:
                if self.maze.laby[self.case_y - 1][self.case_x] != wall:
                    self.case_y -= 1
                    self.y = self.case_y * sprite_size
            self.direction = self.up

        if direction == mv_down:
            if self.case_y < (sprite_side - 1):
                if self.maze.laby[self.case_y + 1][self.case_x] != wall:
                    self.case_y += 1
                    self.y = self.case_y * sprite_size
            self.direction = self.down


