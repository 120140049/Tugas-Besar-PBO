#masi berantakan plz dont judge me biar keliatan uda kerja aja

import pygame

FPS = 30

class Arena:
    def __init__(self):
        self.running = True
        self.window = None
        self.win_size = self.width, self.height = 1270, 720

        pygame.init()
        white = (255, 255, 255)
        self.window = pygame.display.set_mode(self.win_size)
        self.fpsclock = pygame.time.Clock()
        pygame.display.set_caption("Dungeon Figther")
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render('Press A for indoor. Press B for outdoor.', True, white)
        self.textRect = self.text.get_rect()
        self.textRect.center = (1270 // 2, 720 // 2)
      
        self.active_sprite_list = pygame.sprite.Group()

        black = (0, 0, 0)
        self.window.fill(black)
        self.window.blit(self.text, self.textRect)
        while self.running:
            for event in pygame.event.get():
              if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_a:
                      pygame.display.set_caption("Dungeon Figther")
                      bg_img = pygame.image.load('Battleground2.png')
                      icon = pygame.image.load('Battleground2.png')
                      pygame.display.set_icon(icon)
                      self.window.blit(bg_img, (0, 0))
                    
                  elif event.key == pygame.K_b:
                      pygame.display.set_caption("Dungeon Figther")
                      bg_img = pygame.image.load('Battleground4.png')
                      icon = pygame.image.load('Battleground4.png')
                      pygame.display.set_icon(icon)
                      self.window.blit(bg_img, (0, 0))
              if event.type == pygame.KEYUP:
                  self.running = False

            self.active_sprite_list.update()
            self.active_sprite_list.draw(self.window)
            pygame.display.update()
            self.fpsclock.tick(FPS)
          
        pygame.quit()