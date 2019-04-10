import pygame
from config import *
from pygame.locals import *


class Maze:
    
    """ Maze class

        laby = Maze structure
        choice = Level choice

    """
    
    def __init__(self, choice):
        self.laby = 0
        self.choice = choice


    def generate(self):
        
        """ Reading the level file and listing each typographic character """
        
        file = self.choice
        with open(file, "r") as file:
            maze_structure = []
            for line in file:
                maze_line = []
                for sprite in line:
                    if sprite != '\n':
                        maze_line.append(sprite)
                maze_structure.append(maze_line)
            self.laby = maze_structure

    def spriteslaby(self, screen):
        
        """ From the maze's structure, allowing and displaying wall, floor and guardian sprites """
        
        wall_pic = pygame.image.load(wall_sprite).convert()
        floor_pic = pygame.image.load(floor_sprite).convert()
        guardian_pic = pygame.image.load(guardian_sprite).convert_alpha()
        
        num_line = 0
        for line in self.laby:
            num_case = 0
            for sprite in line:
                x = num_case * sprite_size
                y = num_line * sprite_size
                if sprite == wall:
                    screen.blit(wall_pic, (x, y))
                elif sprite == path:
                    screen.blit(floor_pic, (x, y))
                elif sprite == gard:
                    screen.blit(floor_pic, (x, y))
                    screen.blit(guardian_pic, (x, y))
                num_case += 1
            num_line +=1
