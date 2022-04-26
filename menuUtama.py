import pygame, sys

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

pygame.init()

def get_font(size): 
    return pygame.font.SysFont("Times", size)

def menuUtama():
    while True:
        Display = pygame.display.set_mode((896, 504))
        pygame.display.set_caption("Main Menu")
        BG = pygame.image.load("img/bg_pilihTingkatKesulitan.jpeg").convert()
        BG = pygame.transform.scale(BG,(896, 504))
        Display.blit(BG, (0, 0))

        Posisi_Mouse = pygame.mouse.get_pos()

        Text_Judul = get_font(70).render("Dungeon Fighter", True, "red")
        Judul_Rect = Text_Judul.get_rect(center=(448, 80))

        Tombol_start= Button(image=pygame.image.load("img/button1.png"), pos=(450, 230), 
                            text_input="Start", font=get_font(35), base_color="red", hovering_color="White")
        Tombol_options = Button(image=pygame.image.load("img/button1.png"), pos=(450, 340), 
                            text_input="options", font=get_font(35), base_color="red", hovering_color="White")                 

        Display.blit(Text_Judul, Judul_Rect)

        for button in [Tombol_start, Tombol_options]:
            button.changeColor(Posisi_Mouse)
            button.update(Display)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Tombol_start.checkForInput(Posisi_Mouse):
                    print ("start button")
                if Tombol_options.checkForInput(Posisi_Mouse):
                    print ("options button")

        pygame.display.update()

menuUtama()