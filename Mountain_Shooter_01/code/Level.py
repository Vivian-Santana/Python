from code import Entity
from code.EntityFactory import EntityFactory

import pygame

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode # menu_option
        self.entity_list: list[Entity] = [] # self.entity_list será uma lista contendo objetos do tipo Entity.
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg')) # instancia os objs do level 1 e guarda na entity_list
        
    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source = ent.surf, dest = ent.rect)
                ent.move() # invoca o movimento
            pygame.display.flip()
            pass
    