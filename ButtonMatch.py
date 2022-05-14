import pygame
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
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
            
pygame.init()
run = True

def matchButton(Display,heroes,monster):
    
        Posisi_Mouse = pygame.mouse.get_pos()
        Tombol_attack= Button(image=pygame.image.load(f"{game_env}/button1.png"),
            pos=(290, 408), text_input="attack", font=get_font(15),
            base_color="white", hovering_color="red")
        Tombol_skill = Button(image=pygame.image.load(f"{game_env}/button1.png"),
            pos=(600, 408), text_input="skill", font=get_font(15),
            base_color="white", hovering_color="red")

        for button in [Tombol_attack, Tombol_skill]:
            button.changeColor(Posisi_Mouse)
            button.update(Display)

        for event in pygame.event.get():
         if heroes.turn % 2 == 0 and monster.finish and heroes.action == 0 \
                and heroes.onground:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Tombol_attack.checkForInput(Posisi_Mouse):
                    heroes.serang()
                if Tombol_skill.checkForInput(Posisi_Mouse):
                    heroes.serang()
