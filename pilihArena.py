import sys
import pygame
from assetModule import game_env, game_bgm, get_font

FPS = 60
class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
"""
class Arena:
    def __init__(self):
        self.running = True
        self.window = None
        self.win_size = self.width, self.height = 896, 504
        self.bg_img = self.music = self.state = None

        pygame.init()
        self.window = pygame.display.set_mode(self.win_size)
        self.fpsclock = pygame.time.Clock()
        pygame.display.set_caption("Dungeon Figther")
        bg_img = pygame.image.load(f'{game_env}/pilihBGsimple.png').convert_alpha()
        self.window.blit(bg_img, (0, 0))

        Text_Judul = get_font(40).render("Pilih Arena", True, "red")
        Judul_Rect = Text_Judul.get_rect(center=(448, 80))
        self.window.blit(Text_Judul, Judul_Rect)

        Tombol_back = Button(image=pygame.image.load(f"{game_env}/button2.png"),
                            pos=(100, 50), text_input="Back", font=get_font(15),
                            base_color="white", hovering_color="red")

        while self.running:
            Posisi_Mouse = pygame.mouse.get_pos()
            Tombol_back.changeColor(Posisi_Mouse)
            Tombol_back.update(self.window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
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

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Tombol_back.checkForInput(Posisi_Mouse):
                        self.state = 'Back'
                        self.running = False

            pygame.display.flip()
            self.fpsclock.tick(FPS)
"""
class Arena:
    def __init__(self):
        self.running = True
        self.window = None
        self.win_size = self.width, self.height = 896, 504
        self.bg_img = self.music = self.state = None

        pygame.init()
        self.window = pygame.display.set_mode(self.win_size)
        self.fpsclock = pygame.time.Clock()
        pygame.display.set_caption("Pilih Arena")
        bg_img = pygame.image.load(f'{game_env}/bg_pilihTingkatKesulitan.jpeg').convert()
        bg_img= pygame.transform.scale(bg_img,(896, 504))
        self.window.blit(bg_img, (0, 0))

        Text_Judul = get_font(40).render("Pilih Arena", True, "white")
        Judul_Rect = Text_Judul.get_rect(center=(448, 80))
        self.window.blit(Text_Judul, Judul_Rect)

        img1 = pygame.image.load(f'{game_env}/button1.png')
        self.window.blit(img1, (140, 350))
        img2 = pygame.image.load(f'{game_env}/button1.png')
        self.window.blit(img2, (460, 350))

        Tombol_back = Button(image=pygame.image.load(f"{game_env}/button2.png"),
                            pos=(100, 50), text_input="Back", font=get_font(15),
                            base_color="white", hovering_color="red")
        Tombol_arena1= Button(image=pygame.image.load(f'{game_env}/button2.png'), pos=(290, 408), 
                            text_input="Arena 1", font=get_font(15), base_color="white", hovering_color="red")           
        Tombol_arena2 = Button(image=pygame.image.load(f'{game_env}/button2.png'), pos=(610, 408), 
                            text_input="Arena 2", font=get_font(15), base_color="white", hovering_color="red")
        

        while self.running:
            Posisi_Mouse = pygame.mouse.get_pos()
            image_arena = pygame.image.load(f'{game_env}/Battleground0.png')
            
            for button in [Tombol_arena1, Tombol_arena2, Tombol_back]:
                button.changeColor(Posisi_Mouse)
                button.update(self.window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Tombol_arena1.checkForInput(Posisi_Mouse):
                        pygame.display.set_caption("Dungeon Figther")
                        bg_img = pygame.image.load(f'{game_env}/Battleground2.png')
                        self.bg_img = pygame.transform.scale(bg_img, (896, 504))
                        self.music = f'{game_bgm}/bgA.ogg'
                        self.running = False

                    if Tombol_arena2.checkForInput(Posisi_Mouse):
                        pygame.display.set_caption("Dungeon Figther")
                        bg_img = pygame.image.load(f'{game_env}/Battleground4.png')
                        self.bg_img = pygame.transform.scale(bg_img, (896, 504))
                        self.music = f'{game_bgm}/bgB.ogg'
                        self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Tombol_back.checkForInput(Posisi_Mouse):
                        self.state = 'Back'
                        self.running = False
                if Tombol_arena1.checkForInput(Posisi_Mouse):
                            image_arena=pygame.image.load(f'{game_env}/Battleground1.png')
                            self.window.blit(image_arena,(285,130))
                           
                if Tombol_arena2.checkForInput(Posisi_Mouse):
                            image_arena=pygame.image.load(f'{game_env}/Battleground3.png')
                            self.window.blit(image_arena,(285,130))
                           
                self.window.blit(image_arena,(285,130))
            pygame.display.flip()
            self.fpsclock.tick(FPS)