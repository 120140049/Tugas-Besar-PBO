import pygame
from assetModule import game_env, game_bgm

FPS = 60

class Arena:
    def __init__(self):
        self.running = True
        self.window = None
        self.win_size = self.width, self.height = 896, 504
        self.bg_img = self.music = None

        pygame.init()
        self.window = pygame.display.set_mode(self.win_size)
        self.fpsclock = pygame.time.Clock()
        pygame.display.set_caption("Dungeon Figther")
        bg_img = pygame.image.load(f'{game_env}/pilihBGsimple.png').convert_alpha()
        self.window.blit(bg_img, (0, 0))

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        pygame.display.set_caption("Dungeon Figther")
                        bg_img = pygame.image.load(f'{game_env}/Battleground2.png')
                        self.bg_img = pygame.transform.scale(bg_img, (896, 504))
                        self.music = f'{game_bgm}/bgA.ogg'
                        self.running = False

                    elif event.key == pygame.K_b:
                        pygame.display.set_caption("Dungeon Figther")
                        bg_img = pygame.image.load(f'{game_env}/Battleground4.png')
                        self.bg_img = pygame.transform.scale(bg_img, (896, 504))
                        self.music = f'{game_bgm}/bgB.ogg'
                        self.running = False

            pygame.display.flip()
            self.fpsclock.tick(FPS)
