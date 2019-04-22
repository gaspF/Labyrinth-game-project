import pygame
from pygame.locals import *
from gyver import *
from maze import *
from config import *
from availablecase import *

class Game:
    
    """ Main game class

        Displaying game title and icon
        Laby refers to the maze structure

    """
    
    def __init__(self):
        self.laby = 0
        self.victory = 2


    def start_menu(self):
        
        """ Displaying start main menu """
        
        pursue = 1
        
        while pursue:
            
            """ During the loop, displaying and refreshing main menu's screen """
            
            on_main_menu = 1
            screen = pygame.display.set_mode((window_side, window_side))
            main = pygame.image.load(main_menu).convert()
            screen.blit(main, (0,0))
            pygame.display.flip()
        
            while on_main_menu:
                pygame.time.Clock().tick(30)
                
                """ By pressing a key on the main menu, play can Quit or start the game """
                
                for event in pygame.event.get():
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        on_main_menu = 0
                        pursue = 0

                    elif event.type == KEYDOWN and event.key == K_F1:
                        on_main_menu = 0
                        Game.start_game(self)



    def start_game(self):

        """ Starting new game

        dropped_needle, dropped_tube, dropped_ether = Variables that define if player get the items in the inventory
        screen = Displaying new screen for the game
        maze = construct the maze and display it with spriteslaby method
        choice = level name, which is located in config
        giver = creating the main character
        Three pictures are allowed to needle, tube and ether. Then, the items are placed randomly and displayed in the maze

        """
        
        continue_game = 1
        ending_screen = 0
        dropped_needle = 1
        dropped_tube = 1
        dropped_ether = 1
        pygame.time.Clock().tick(30)
        screen = pygame.display.set_mode((window_side, 700))
        
        maze = Maze(choice)
        maze.generate()
        maze.spriteslaby(screen)
        
        giver = Mcgiver(right_giver_sprite, left_giver_sprite, up_giver_sprite, down_giver_sprite, maze)
        
        etherIMG = pygame.image.load(sprite_ether_dp).convert_alpha()
        needleIMG = pygame.image.load(sprite_needle_dp).convert_alpha()
        tubeIMG = pygame.image.load(sprite_tube_dp).convert_alpha()
        
        ether = AvailableCase(etherIMG, maze)
        needle = AvailableCase(needleIMG, maze)
        tube = AvailableCase(tubeIMG, maze) 
        
        ether.display(etherIMG, screen)
        needle.display(needleIMG, screen)
        tube.display(tubeIMG, screen) 

        while continue_game:
            
            """ During the loop, player can quit the game or move the character by pressing the following keys """
            
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    continue_game = 0
                    pursue = 0
        
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.continue_game = 0
                    elif event.key == K_RIGHT:
                        giver.move(mv_right)
                    elif event.key == K_LEFT:
                        giver.move(mv_left)
                    elif event.key == K_UP:
                        giver.move(mv_up)
                    elif event.key == K_DOWN:
                        giver.move(mv_down)
                        
            """ Refreshing the sprites after movement """
            
            maze.spriteslaby(screen)
            screen.blit(giver.direction, (giver.x, giver.y))

            """ If player move on one of the following items, item will be moved into the inventory """
            
            if dropped_ether:
                screen.blit(ether.attribute_picture, (ether.x, ether.y))
            if (giver.x, giver.y) == (ether.x, ether.y):
                dropped_ether = False
                screen.blit(ether.attribute_picture, (50, 650))

            if dropped_tube:
                screen.blit(tube.attribute_picture, (tube.x, tube.y))
            if (giver.x, giver.y) == (tube.x, tube.y):
                dropped_tube = False
                screen.blit(tube.attribute_picture, (0, 650))

            if dropped_needle:
                screen.blit(needle.attribute_picture, (needle.x, needle.y))
            if (giver.x, giver.y) == (needle.x, needle.y):
                dropped_needle = False
                screen.blit(needle.attribute_picture, (100, 650))

            pygame.display.flip()
            
            """ Victory or loose conditions. Player must have all the items to kill the guardian"""
            
            if maze.laby[giver.case_x][giver.case_y] == gard:
                if dropped_tube is False and dropped_ether is False and dropped_needle is False:
                    victory = True
                    continue_game = False
                    ending_screen = True

                    
                else:
                    victory = False
                    continue_game = False
                    ending_screen = True

        while ending_screen:
            
            """ displaying victory or loose screen on a new window. Player can quit the screen by pressing Escape """
            
            if victory:
                pygame.time.Clock().tick(30)
                screen = pygame.display.set_mode((window_side, window_side))
                vic_screen = pygame.image.load(game_victory).convert()
                screen.blit(vic_screen, (0,0))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        ending_screen = False
                
            else:
                pygame.time.Clock().tick(30)
                screen = pygame.display.set_mode((window_side, window_side))
                loose_screen = pygame.image.load(game_loose).convert()
                screen.blit(loose_screen, (0,0))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        ending_screen = False


