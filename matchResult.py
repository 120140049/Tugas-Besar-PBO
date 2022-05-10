import pygame, sys
from assetModule import game_env, get_font

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
		if position[0] in range(self.rect.left, self.rect.right) and \
            position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and \
            position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

pygame.init()

def akhirpertandingan(arena, grounds):
    while True:
        Display = pygame.display.set_mode((896, 504))
        pygame.display.set_caption("Dungeon Fighter")
        Display.blit(arena, (0, 0))
        grounds.draw(Display)

        Posisi_Mouse = pygame.mouse.get_pos()

        Text_Judul = get_font(35).render("Permainan Selesai", True, "red")
        Judul_Rect = Text_Judul.get_rect(center=(448, 80))

        Tombol_menu = Button(image=pygame.image.load(f"{game_env}/button1.png"),
                            pos=(450, 400), text_input="Menu", font=get_font(18),
                            base_color="white", hovering_color="Red")
        Tombol_back = Button(image=pygame.image.load(f"{game_env}/button1.png"),
                            pos=(450, 300), text_input="Main lagi",
                            font=get_font(18), base_color="white", hovering_color="red")                   

        Display.blit(Text_Judul, Judul_Rect)

        for button in [Tombol_menu,Tombol_back]:
            button.changeColor(Posisi_Mouse)
            button.update(Display)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Tombol_menu.checkForInput(Posisi_Mouse):
                    #ubah HP monster dan damage 
                    return True
                if Tombol_back.checkForInput(Posisi_Mouse):
                    #kembali ke pilih Arena
                    return False

        pygame.display.update()