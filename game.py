import pygame
import player

FPS = 30

class Game:
    def __init__(self):
        self.running = True
        self.window = None
        self.win_size = self.width, self.height = 1270, 720

    def make_window(self):
        pygame.init()
        self.window = pygame.display.set_mode(self.win_size)
        self.fpsclock = pygame.time.Clock()
        pygame.display.set_caption("Dungeon Figther")
        bg_img = pygame.image.load('img/bg2.png')
        icon = pygame.image.load('img/bg2.png')
        pygame.display.set_icon(icon)
        self.window.blit(bg_img, (0, 90))

    def play_game(self):
        self.active_sprite_list = pygame.sprite.Group()
        self.select_character()

        self.make_window()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.active_sprite_list.update()
            self.active_sprite_list.draw(self.window)
            pygame.display.update()
            self.fpsclock.tick(FPS)

        pygame.quit()


    def select_character(self):
        # print("1.Ulrich\n2.Lu Bu\n3.Zeus")
        # self.karakter_pilihan = int(input("Masukkan pilihan: "))
        # print("1.Demonzilla\n2. DOOM")
        # self.monster_pilihan = int(input("Masukkan pilihan: "))
        players = player.Ulrich()
        enemy = player.Demonzilla()
        self.active_sprite_list.add(players)
        self.active_sprite_list.add(enemy)
        players.rect.x = 75
        players.rect.y = self.height - 220
        enemy.rect.x = 1125
        enemy.rect.y = self.height - 270

if __name__ == "__main__":
    StreetFighter = Game()
    StreetFighter.play_game()
