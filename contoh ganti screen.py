from turtle import Screen
import pygame, sys, os, pygame_widgets


class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color
        self.hovering_color =  hovering_color
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
                    pilihhero()
                if Tombol_options.checkForInput(Posisi_Mouse):
                    print ("options button")
                    pilihTingkatKesulitan()

        pygame.display.update()

def pilihhero():
      while True:
        Display = pygame.display.set_mode((896, 504))
        pygame.display.set_caption("Display Pilih Hero")
        BG = pygame.image.load("img/bg_pilihTingkatKesulitan.jpeg").convert()
        BG = pygame.transform.scale(BG,(896, 504))
        Display.blit(BG, (0, 0))

        Posisi_Mouse = pygame.mouse.get_pos()

        Text_Judul = get_font(70).render("Pilih Hero", True, "red")
        Judul_Rect = Text_Judul.get_rect(center=(448, 80))

        Tombol_alectrona= Button(image=pygame.image.load("img/button1.png"), pos=(200, 180), 
                            text_input="Alectrona", font=get_font(35), base_color="red", hovering_color="White")
        Tombol_nipalto = Button(image=pygame.image.load("img/button1.png"), pos=(200, 290), 
                            text_input="Nipalto", font=get_font(35), base_color="red", hovering_color="White")
        Tombol_salazar = Button(image=pygame.image.load("img/button1.png"), pos=(200, 400), 
                            text_input="Salazar", font=get_font(35), base_color="red", hovering_color="White")
        Tombol_back = Button(image=pygame.image.load("img/button2.png"), pos=(30, 50), 
                            text_input="Back", font=get_font(20), base_color="red", hovering_color="White")                   

        Display.blit(Text_Judul, Judul_Rect)

        CWD=os.getcwd()
        pathfile=os.path.join(CWD, "img/pilihKarakter")
        image_base = pygame.image.load(os.path.join(pathfile,'unknownchar.png'))
        #image_base = image_info.get_rect(center = (530,82))


        #pos_info=(530,82)

        for button in [Tombol_alectrona, Tombol_nipalto, Tombol_salazar,Tombol_back]:
            button.changeColor(Posisi_Mouse)
            button.update(Display)
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Tombol_alectrona.checkForInput(Posisi_Mouse):
                    #ubah HP monster dan damage 
                    print ("easy button")
                    pilihmonster()
                if Tombol_nipalto.checkForInput(Posisi_Mouse):
                    #ubah HP monster dan damage 
                    print ("medium button")
                    pilihmonster()
                if Tombol_salazar.checkForInput(Posisi_Mouse):
                    #ubah HP monster dan damage 
                    print ("hard button")
                    pilihmonster()
                if Tombol_back.checkForInput(Posisi_Mouse):
                    #kembali ke pilih Arena
                    print ("back button")
                    menuUtama()
            
        if Tombol_alectrona.checkForInput(Posisi_Mouse):
            image_base=pygame.image.load(os.path.join(pathfile,'infoAlectrona.png'))
            Display.blit(image_base,(450,130))
        if Tombol_nipalto.checkForInput(Posisi_Mouse):
            image_base=pygame.image.load(os.path.join(pathfile,'infoNipalto.png'))
            Display.blit(image_base,(450,130))
        if Tombol_salazar.checkForInput(Posisi_Mouse):
            image_base=pygame.image.load(os.path.join(pathfile,'infoSalazar.png'))
            Display.blit(image_base,(450,130))
                
        Display.blit(image_base,(450,130))
        pygame_widgets.update(event)

        pygame.display.update()

def pilihmonster():
     while True:
        Display = pygame.display.set_mode((896, 504))
        pygame.display.set_caption("Display Pilih Monster")
        BG = pygame.image.load("img/bg_pilihTingkatKesulitan.jpeg").convert()
        BG = pygame.transform.scale(BG,(896, 504))
        Display.blit(BG, (0, 0))

        Posisi_Mouse = pygame.mouse.get_pos()

        Text_Judul = get_font(70).render("Pilih Monster", True, "red")
        Judul_Rect = Text_Judul.get_rect(center=(448, 80))

        Tombol_aposteus= Button(image=pygame.image.load("img/button1.png"), pos=(200, 180), 
                            text_input="aposteus", font=get_font(35), base_color="red", hovering_color="White")
        Tombol_fenrir = Button(image=pygame.image.load("img/button1.png"), pos=(200, 290), 
                            text_input="fenrir", font=get_font(35), base_color="red", hovering_color="White")
        Tombol_back = Button(image=pygame.image.load("img/button2.png"), pos=(30, 50), 
                            text_input="Back", font=get_font(20), base_color="red", hovering_color="White")                   

        Display.blit(Text_Judul, Judul_Rect)

        CWD=os.getcwd()
        pathfile=os.path.join(CWD, "img/pilihKarakter")
        image_base = pygame.image.load(os.path.join(pathfile,'unknownchar.png'))
        #image_base = image_info.get_rect(center = (530,82))


        #pos_info=(530,82)

        for button in [Tombol_aposteus, Tombol_fenrir,Tombol_back]:
            button.changeColor(Posisi_Mouse)
            button.update(Display)
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Tombol_aposteus.checkForInput(Posisi_Mouse):
                    #ubah HP monster dan damage 
                    print ("easy button")
                    pilihArena()
                if Tombol_fenrir.checkForInput(Posisi_Mouse):
                    #ubah HP monster dan damage 
                    print ("medium button")
                    pilihArena()
                if Tombol_back.checkForInput(Posisi_Mouse):
                    #kembali ke pilih Arena
                    print ("back button")
                    pilihhero()
            
        if Tombol_aposteus.checkForInput(Posisi_Mouse):
            image_base=pygame.image.load(os.path.join(pathfile,'infoAposteus.png'))
            Display.blit(image_base,(450,130))
        if Tombol_fenrir.checkForInput(Posisi_Mouse):
            image_base=pygame.image.load(os.path.join(pathfile,'infoFenrir.png'))
            Display.blit(image_base,(450,130))
                
        Display.blit(image_base,(450,130))
        pygame_widgets.update(event)

        pygame.display.update()

def pilihArena():
    while True:
        Display = pygame.display.set_mode((896, 504))
        pygame.display.set_caption("Display Pilih Arena")
        BG = pygame.image.load("img/bg_pilihTingkatKesulitan.jpeg").convert()
        BG = pygame.transform.scale(BG,(896, 504))
        Display.blit(BG, (0, 0))

        Posisi_Mouse = pygame.mouse.get_pos()

        Text_Judul = get_font(70).render("Pilih Arena", True, "red")
        Judul_Rect = Text_Judul.get_rect(center=(448, 80))

        Tombol_arena1= Button(image=pygame.image.load("img/button1.png"), pos=(300, 400), 
                            text_input="Arena 1", font=get_font(35), base_color="red", hovering_color="White")
        Tombol_arena2 = Button(image=pygame.image.load("img/button1.png"), pos=(600, 400), 
                            text_input="Arena 2", font=get_font(35), base_color="red", hovering_color="White")
        Tombol_back = Button(image=pygame.image.load("img/button2.png"), pos=(30, 50), 
                            text_input="Back", font=get_font(20), base_color="red", hovering_color="White")                   

        Display.blit(Text_Judul, Judul_Rect)

        CWD=os.getcwd()
        pathfile=os.path.join(CWD, "img")
        image_base = pygame.image.load(os.path.join(pathfile,'Battleground0.jpg'))
        #image_base = image_info.get_rect(center = (530,82))


        #pos_info=(530,82)

        for button in [Tombol_arena1, Tombol_arena2,Tombol_back]:
            button.changeColor(Posisi_Mouse)
            button.update(Display)
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Tombol_arena1.checkForInput(Posisi_Mouse):
                    #ubah HP monster dan damage 
                    print ("easy button")
                    pilihTingkatKesulitan()
                if Tombol_arena2.checkForInput(Posisi_Mouse):
                    #ubah HP monster dan damage 
                    print ("medium button")
                    pilihTingkatKesulitan()
                if Tombol_back.checkForInput(Posisi_Mouse):
                    #kembali ke pilih Arena
                    print ("back button")
                    pilihmonster()
            
        if Tombol_arena1.checkForInput(Posisi_Mouse):
            image_base=pygame.image.load(os.path.join(pathfile,'Battleground1.png'))
            Display.blit(image_base,(285,130))
        if Tombol_arena2.checkForInput(Posisi_Mouse):
            image_base=pygame.image.load(os.path.join(pathfile,'Battleground3.png'))
            Display.blit(image_base,(285,130))
                
        Display.blit(image_base,(285,130))
        pygame_widgets.update(event)

        pygame.display.update()

def pilihTingkatKesulitan():
    while True:
        Display = pygame.display.set_mode((896, 504))
        pygame.display.set_caption("Display Tingkat Kesulitan")
        BG = pygame.image.load("img/bg_pilihTingkatKesulitan.jpeg").convert()
        BG = pygame.transform.scale(BG,(896, 504))
        Display.blit(BG, (0, 0))

        Posisi_Mouse = pygame.mouse.get_pos()

        Text_Judul = get_font(70).render("Tingkat Kesulitan", True, "red")
        Judul_Rect = Text_Judul.get_rect(center=(448, 80))

        Tombol_easy= Button(image=pygame.image.load("img/button1.png"), pos=(450, 180), 
                            text_input="Easy", font=get_font(35), base_color="red", hovering_color="White")
        Tombol_medium = Button(image=pygame.image.load("img/button1.png"), pos=(450, 290), 
                            text_input="Medium", font=get_font(35), base_color="red", hovering_color="White")
        Tombol_hard = Button(image=pygame.image.load("img/button1.png"), pos=(450, 400), 
                            text_input="Hard", font=get_font(35), base_color="red", hovering_color="White")
        Tombol_back = Button(image=pygame.image.load("img/button2.png"), pos=(30, 50), 
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
                    game()
                if Tombol_medium.checkForInput(Posisi_Mouse):
                    #ubah HP monster dan damage 
                    print ("medium button")
                    game()
                if Tombol_hard.checkForInput(Posisi_Mouse):
                    #ubah HP monster dan damage 
                    print ("hard button")
                    game()
                if Tombol_back.checkForInput(Posisi_Mouse):
                    #kembali ke pilih Arena
                    print ("back button")
                    pilihArena()

        pygame.display.update()

def game():
    while True:
        Display = pygame.display.set_mode((896, 504))
        pygame.display.set_caption("Display Game")
        BG = pygame.image.load("img/bg_pilihTingkatKesulitan.jpeg").convert()
        BG = pygame.transform.scale(BG,(896, 504))
        Display.blit(BG, (0, 0))
        
        Posisi_Mouse = pygame.mouse.get_pos()

        Text_Judul = get_font(70).render(" ", True, "red")
        Judul_Rect = Text_Judul.get_rect(center=(448, 80))

        Tombol_back = Button(image=pygame.image.load("img/button1.png"), pos=(450, 300), 
                            text_input="GAME", font=get_font(40), base_color="red", hovering_color="White")                   

        Display.blit(Text_Judul, Judul_Rect)

        for button in [Tombol_back]:
            button.changeColor(Posisi_Mouse)
            button.update(Display)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Tombol_back.checkForInput(Posisi_Mouse):
                    #kembali ke pilih Arena
                    print ("back button")
                    akhirpertandingan()

        pygame.display.update()

def akhirpertandingan():
    while True:
        Display = pygame.display.set_mode((896, 504))
        pygame.display.set_caption("Display Permainan Selesai")
        BG = pygame.image.load("img/Battleground4.png").convert()
        BG = pygame.transform.scale(BG,(896, 504))
        Display.blit(BG, (0, 0))

        Posisi_Mouse = pygame.mouse.get_pos()

        Text_Judul = get_font(70).render("Permainan Selesai", True, "red")
        Judul_Rect = Text_Judul.get_rect(center=(448, 80))

        Tombol_menu = Button(image=pygame.image.load("img/button1.png"), pos=(450, 400), 
                            text_input="Menu", font=get_font(35), base_color="red", hovering_color="White")
        Tombol_back = Button(image=pygame.image.load("img/button1.png"), pos=(450, 300), 
                            text_input="Main lagi", font=get_font(35), base_color="red", hovering_color="White")                   

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
                    print ("menu")
                    menuUtama()
                if Tombol_back.checkForInput(Posisi_Mouse):
                    #kembali ke pilih Arena
                    print ("main lagi")
                    menuUtama()

        pygame.display.update()

if __name__ == "__main__":
    menuUtama()


