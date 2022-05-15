import pygame, sys
from assetModule import game_env, get_font

state = None
run = True

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

def menuUtama():
    global run, state
    while run == True:
        Display = pygame.display.set_mode((896, 504))
        pygame.display.set_caption("Main Menu")
        BG = pygame.image.load(f"{game_env}/bg_pilihTingkatKesulitan.jpeg").convert()
        BG = pygame.transform.scale(BG,(896, 504))
        Display.blit(BG, (0, 0))

        Posisi_Mouse = pygame.mouse.get_pos()

        Text_Judul = get_font(35).render("Dungeon Fighter", True, "red")
        Judul_Rect = Text_Judul.get_rect(center=(448, 80))

        Tombol_start= Button(image=pygame.image.load(f"{game_env}/button1.png"), 
                            pos=(450, 230), text_input="Start", font=get_font(20),
                            base_color="white", hovering_color="red")
        Tombol_exit = Button(image=pygame.image.load(f"{game_env}/button1.png"),
                            pos=(450, 340), text_input="Exit", font=get_font(20),
                            base_color="white", hovering_color="red")                 

        Display.blit(Text_Judul, Judul_Rect)

        for button in [Tombol_start, Tombol_exit]:
            button.changeColor(Posisi_Mouse)
            button.update(Display)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Tombol_start.checkForInput(Posisi_Mouse):
                    state = 'Start'
                    return state
                    run = False
                if Tombol_exit.checkForInput(Posisi_Mouse):
                    state = 'Options'
                    return state
                    run = False

        pygame.display.update()


def matchButton():
	Tombol_attack= Button(image=pygame.image.load(f"{game_env}/button1.png"),
		pos=(290, 450), text_input="attack", font=get_font(15),
		base_color="white", hovering_color="red")
	Tombol_skill = Button(image=pygame.image.load(f"{game_env}/button1.png"),
		pos=(600, 450), text_input="skill", font=get_font(15),
		base_color="white", hovering_color="red")

	return [Tombol_attack, Tombol_skill]