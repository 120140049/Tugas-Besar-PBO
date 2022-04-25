#belom ngerti cara ngoper bg dari sini ke main

import pygame
from pygame import mixer

FPS = 30

class Arena:
    def __init__(self):
        self.running = True
        self.window = None
        self.win_size = self.width, self.height = 896, 504

        pygame.init()
        mixer.init()
        self.window = pygame.display.set_mode(self.win_size)
        self.fpsclock = pygame.time.Clock()
        pygame.display.set_caption("Dungeon Figther")
        bg_img = pygame.image.load('img/pilihBGsimple.png').convert_alpha()
        self.window.blit(bg_img, (0, 0))      
              
        while self.running:
            for event in pygame.event.get():
              if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_a:
                      pygame.display.set_caption("Dungeon Figther")
                      bg_img = pygame.image.load('img/Battleground2.png')
                      icon = pygame.image.load('img/Battleground2.png')
                      pygame.display.set_icon(icon)
                      self.window.blit(bg_img, (0, 0))
                      mixer.music.load('bgm/bgA.ogg')
                      mixer.music.play()
                    
                  elif event.key == pygame.K_b:
                      pygame.display.set_caption("Dungeon Figther")
                      bg_img = pygame.image.load('img/Battleground4.png')
                      icon = pygame.image.load('img/Battleground4.png')
                      pygame.display.set_icon(icon)
                      self.window.blit(bg_img, (0, 0))
                      mixer.music.load('bgm/bgB.ogg')
                      mixer.music.play()
                    
              if event.type == pygame.KEYUP:
                  pygame.display.update()
                  self.fpsclock.tick(FPS)
                  self.running = False

            pygame.display.update()
            self.fpsclock.tick(FPS)
