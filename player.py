import pygame
import character


WHITE = (255,255,255)
BLACK = (0,0,0)

class Ulrich(pygame.sprite.Sprite, character.Hero):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        character.Hero.__init__(self, "Ulrich", 3200, 245)

        self.image = pygame.Surface([50, 80])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()

    def serang(self):
        pass

class Demonzilla(pygame.sprite.Sprite, character.Monster):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        character.Monster.__init__(self, "Demonzilla", 3200, 245)

        self.image = pygame.Surface([70, 120])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()

    def serang(self):
        pass
