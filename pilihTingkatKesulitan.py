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

def tingkatKesulitan():
    while True:
        Display = pygame.display.set_mode((896, 504))
        pygame.display.set_caption("Display Tingkat Kesulitan")
        BG = pygame.image.load("Assets/env/bg_pilihTingkatKesulitan.jpeg").convert()
        BG = pygame.transform.scale(BG,(896, 504))
        Display.blit(BG, (0, 0))

        Posisi_Mouse = pygame.mouse.get_pos()

        Text_Judul = get_font(70).render("Tingkat Kesulitan", True, "red")
        Judul_Rect = Text_Judul.get_rect(center=(448, 80))

        Tombol_easy= Button(image=pygame.image.load("Assets/env/button1.png"), pos=(450, 180), 
                            text_input="Easy", font=get_font(35), base_color="red", hovering_color="White")
        Tombol_medium = Button(image=pygame.image.load("Assets/env/button1.png"), pos=(450, 290), 
                            text_input="Medium", font=get_font(35), base_color="red", hovering_color="White")
        Tombol_hard = Button(image=pygame.image.load("Assets/env/button1.png"), pos=(450, 400), 
                            text_input="Hard", font=get_font(35), base_color="red", hovering_color="White")
        Tombol_back = Button(image=pygame.image.load("Assets/env/button2.png"), pos=(30, 50), 
                            text_input="Back", font=get_font(20), base_color="red", hovering_color="White")                   

        Display.blit(Text_Judul, Judul_Rect)

        for button in [Tombol_easy, Tombol_medium, Tombol_hard,Tombol_back]:
            button.changeColor(Posisi_Mouse)
            button.update(Display)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Tombol_easy.checkForInput(Posisi_Mouse):
                    #ubah HP monster dan damage 
                    print ("easy button")
                if Tombol_medium.checkForInput(Posisi_Mouse):
                    #meningkatkanh HP dan damage monster sebesar 115%
                    print ("medium button")
                if Tombol_hard.checkForInput(Posisi_Mouse):
                    #meningkatkanh HP dan damage monster sebesar 125%
                    print ("hard button")
                if Tombol_back.checkForInput(Posisi_Mouse):
                    #kembali ke display pilih Arena
                    print ("back button")

        pygame.display.update()
<<<<<<< HEAD
=======

tingkatKesulitan()
>>>>>>> bee434e12c133324c9281016b8e250454556123e
