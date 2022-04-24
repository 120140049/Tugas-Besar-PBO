import pygame
import character


WHITE = (255,255,255)
BLACK = (0,0,0)

class Alectrona(pygame.sprite.Sprite, character.Hero):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        character.Hero.__init__(self, "Alectrona", 3000, 200)

        self.image = pygame.Surface([50, 80])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()

    def serang(self):
        pass

class Nipalto(pygame.sprite.Sprite, character.Hero):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        character.Hero.__init__(self, "Nipalto", 2500, 275)

        self.image = pygame.Surface([50, 80])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()

    def serang(self):
        pass

class Salazar(pygame.sprite.Sprite, character.Hero):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        character.Hero.__init__(self, "Salazar", 2000, 350)

        self.image = pygame.Surface([50, 80])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()

    def serang(self):
        pass

class Aposteus(pygame.sprite.Sprite, character.Monster):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        character.Monster.__init__(self, "Aposteus", 5000, 25)

        self.image = pygame.Surface([70, 120])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()

    def serang(self):
        pass

class Fenrir(pygame.sprite.Sprite, character.Monster):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        character.Monster.__init__(self, "Fenrir", 3000, 50)

        self.image = pygame.Surface([70, 120])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()

    def serang(self):
        pass
