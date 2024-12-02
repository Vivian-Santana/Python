from abc import ABC, abstractmethod
import pygame

# classe abstrata
class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png') # define um caminho generico para carregar as imagens
        self.rect = self.surf.get_rect(left = position[0], top = position[1]) # define uma posição generica para o retângulo
        self.speed = 0

    @abstractmethod # decorator
    def move(self, ):
        pass