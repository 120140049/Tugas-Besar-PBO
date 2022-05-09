# #baru bikin aja
# #ntar ajala kerjainnya

"""
import pygame
import sys
import pygame_widgets
from pygame_widgets.button import Button
import os
import player

CWD=os.getcwd()
pathfile=os.path.join(CWD, "img/pilihKarakter")
pygame.init()
layar = pygame.display.set_mode((896,504))
main_font=pygame.font.Font("font/A Goblin Appears!.otf",35)
pos_info=(530,82)
pos_mode=(5,82)
dimensi_ava=(110,70)
info_karakter=pygame.image.load(os.path.join(pathfile,'unknownchar.png'))
Hero=None
Monster=None
klik=None
mode_pilihHero=None
mode_pilihMonster=None
cek_pilih_hero=True
cek_pilih_monster=False
teks_karakter=main_font.render(" ? ? ? ? ? ",True,'white')
karakter=None


#assets (tutup hero monster, ava, background, gambar info)

#gambar tutup
mode_pilihHero=pygame.image.load(os.path.join(pathfile,'mode pilih hero.png'))
mode_pilihMonster=pygame.image.load(os.path.join(pathfile,'mode pilih monster.png'))
mode=mode_pilihHero
#gambar ava
avaAlectrona=pygame.image.load(os.path.join(pathfile,'avaAlectrona.png'))
avaNipalto=pygame.image.load(os.path.join(pathfile,'avaNipalto.png'))
avaSalazar=pygame.image.load(os.path.join(pathfile,'avaSalazar.png'))
avaAposteus=pygame.image.load(os.path.join(pathfile,'avaAposteus.png'))
avaFenrir=pygame.image.load(os.path.join(pathfile,'avaFenrir.png'))
#gambar background
background=pygame.image.load(os.path.join(pathfile,'bg_pilihKarakter.jpeg'))
background=pygame.transform.scale(background,(896,504))    

#gambar info
info_alectrona=pygame.image.load(os.path.join(pathfile,'infoAlectrona.png'))
info_nipalto=pygame.image.load(os.path.join(pathfile,'infoNipalto.png'))
info_salazar=pygame.image.load(os.path.join(pathfile,'infoSalazar.png'))
info_aposteus=pygame.image.load(os.path.join(pathfile,'infoAposteus.png'))
info_fenrir=pygame.image.load(os.path.join(pathfile,'infoFenrir.png'))

#kelas tombol tombol opsi pemain
class TombolPilihan():
    pilihan_karakter=[]
    def __init__(self, pos_x, pos_y, nama_karakter,gambar_info,karakter):
        self.nama_karakter=nama_karakter
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.gambar_info=gambar_info
        self.karakter=karakter
        TombolPilihan.generate(self)
     #bikin supaya tombol baru bisa dibikin sesuai atribut   
    def generate(self):
        tombol= Button(
            layar,
            self.pos_x,
            self.pos_y,
            381,
            70,
            text=self.nama_karakter,
            textColour=(255, 255, 255),
            fontSize=65,
            textHAlign=('left'),
            font=pygame.font.Font("font/A Goblin Appears!.otf",35),
            inactiveColour=(175, 118, 140),
            hoverColour=(216, 191, 159),
            onClick=lambda: update(self) 
            )
        TombolPilihan.pilihan_karakter.append(tombol)

#update gambar info dan tulisan nama karakter tiap tombol
def update (objektombol):
    global info_karakter,klik,teks_karakter,karakter
    klik=True
    info_karakter=objektombol.gambar_info
    teks_karakter=main_font.render(objektombol.nama_karakter,True,'white')
    karakter=objektombol.karakter

def nextCommand():
    global cek_pilih_hero,cek_pilih_monster
    if Hero == None and Monster == None : 
        cek_pilih_monster=False
        pilihHero()
    elif Hero != None and Monster == None : 
        cek_pilih_hero=False
        pilihMonster()
    elif Hero != None and Monster != None : print("Step Selanjutnya")

def pilihHero():
    global mode, pos_mode,tombolAlectrona,tombolNipalto,tombolSalazar,cek_pilih_hero,Hero
    cek_pilih_hero=True
    #cetak tombol-tombol ke layar
    tombolAlectrona=TombolPilihan(115,82,"Alectrona",info_alectrona,player.Alectrona())
    tombolNipalto=TombolPilihan(115,160,"Nipalto",info_nipalto,player.Nipalto())
    tombolSalazar=TombolPilihan(115,239,"Salazar",info_salazar,player.Salazar())
    #cetak gambar informasi mode
    mode=mode_pilihHero
    pos_mode=(5,317)
    Hero=karakter


def pilihMonster():
    global mode, pos_mode,tombolAposteus,tombolFenrir,cek_pilih_monster,cek_pilih_hero,Monster
    cek_pilih_hero=False
    cek_pilih_monster=True
    #cetak tombol-tombol ke layar
    tombolAposteus=TombolPilihan(115,317,"Aposteus",info_aposteus,player.Aposteus())
    tombolFenrir=TombolPilihan(115,395,"Fenrir",info_fenrir,player.Fenrir())
    #cetak gambar informasi mode
    mode=mode_pilihMonster
    pos_mode=(5,82)
    Monster=karakter



tombol_back=Button(
    layar,
    36,
    19,
    110,
    50,

    text="BACK",
    font=pygame.font.Font("font/A Goblin Appears!.otf",20),
    textColour='white',
    hoverColour=(128,0,0),
    inactiveColour=(217, 17, 17),
    onClick=lambda: print('Tombol back')
)

tombol_next=Button(
    layar,
    160,
    19,
    110,
    50,

    text="NEXT",
    font=pygame.font.Font("font/A Goblin Appears!.otf",20),
    textColour='white',
    hoverColour=(124, 145, 153),
    inactiveColour=(177, 212, 224),
    onClick=lambda: nextCommand()
)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pilihHero()
    layar.fill("white")
    layar.blit(background,(0,0))
    layar.blit(info_karakter,(530,82))
    pygame_widgets.update(event)
    if cek_pilih_hero:
        #ini ava Alectrona
        layar.blit(avaAlectrona,(5,82))
        #ini ava Nipalto
        layar.blit(avaNipalto,(5,160))
        #ini ava Salazar
        layar.blit(avaSalazar,(5,239))
    if cek_pilih_monster:
        #ini ava Aposteus
        layar.blit(avaAposteus,(5,317))
        #ini ava Fenrir
        layar.blit(avaFenrir,(5,395))

    if klik:
        #ini nanti buat gambar info_karakter
        layar.blit(info_karakter,(530,82))

    #ini buat nama karakter dibawah foto info
    layar.blit(teks_karakter,(510,415))
    #
    layar.blit(mode,pos_mode)
    #taro paling bawah, ini buat update semua perubahan
    pygame.display.update()
"""
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
