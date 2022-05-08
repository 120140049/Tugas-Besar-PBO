# #baru bikin aja
# #ntar ajala kerjainnya
import pygame
import sys
import pygame_widgets
from pygame_widgets.button import Button
import os
import karakter

CWD = os.getcwd()
pathfile = os.path.join(CWD, "Assets/pilihKarakter")
pygame.init()
layar = pygame.display.set_mode((896,504))
main_font = pygame.font.Font("Assets/font/A Goblin Appears!.otf",35)
pos_info = (530,82)
pos_mode = (5,82)
dimensi_ava = (110,70)
info_karakter = pygame.image.load(os.path.join(pathfile,'unknownchar.png'))
Hero = Monster = klik = mode_pilihHero = mode_pilihMonster = karakter = None
cek_pilih_hero = True
cek_pilih_monster = False
teks_karakter = main_font.render(" ? ? ? ? ? ",True,'white')
#assets (tutup hero monster, ava, background, gambar info)

#gambar tutup
mode_pilihHero = pygame.image.load(os.path.join(pathfile,'mode pilih hero.png'))
mode_pilihMonster = pygame.image.load(os.path.join(pathfile,'mode pilih monster.png'))
mode = mode_pilihHero
#gambar ava
avaAlectrona = pygame.image.load(os.path.join(pathfile,'avaAlectrona.png'))
avaNipalto = pygame.image.load(os.path.join(pathfile,'avaNipalto.png'))
avaSalazar = pygame.image.load(os.path.join(pathfile,'avaSalazar.png'))
avaAposteus = pygame.image.load(os.path.join(pathfile,'avaAposteus.png'))
avaFenrir = pygame.image.load(os.path.join(pathfile,'avaFenrir.png'))
#gambar background
background = pygame.image.load(os.path.join(pathfile,'bg_pilihKarakter.jpeg'))
background = pygame.transform.scale(background,(896,504))    

#gambar info
info_alectrona = pygame.image.load(os.path.join(pathfile,'infoAlectrona.png'))
info_nipalto = pygame.image.load(os.path.join(pathfile,'infoNipalto.png'))
info_salazar = pygame.image.load(os.path.join(pathfile,'infoSalazar.png'))
info_aposteus = pygame.image.load(os.path.join(pathfile,'infoAposteus.png'))
info_fenrir = pygame.image.load(os.path.join(pathfile,'infoFenrir.png'))

#kelas tombol tombol opsi pemain
class TombolPilihan():
    pilihan_karakter=[]
    def __init__(self, pos_x, pos_y, nama_karakter, gambar_info):
        self.nama_karakter = nama_karakter
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.gambar_info = gambar_info
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
            font=pygame.font.Font("Assets/font/A Goblin Appears!.otf",35),
            inactiveColour=(175, 118, 140),
            hoverColour=(216, 191, 159),
            onClick=lambda: update(self) 
            )
        TombolPilihan.pilihan_karakter.append(tombol)

#update gambar info dan tulisan nama karakter tiap tombol
def update(objektombol):
    global info_karakter, klik,teks_karakter, karakter
    klik = True
    info_karakter = objektombol.gambar_info
    teks_karakter = main_font.render(objektombol.nama_karakter,True,'white')
    # karakter = objektombol.karakter

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
    global mode, pos_mode, tombolAlectrona, tombolNipalto, tombolSalazar, \
            cek_pilih_hero, Hero
    cek_pilih_hero = True
    #cetak tombol-tombol ke layar
    tombolAlectrona = TombolPilihan(115, 82, "Alectrona", info_alectrona)
    tombolNipalto = TombolPilihan(115,160,"Nipalto",info_nipalto)
    tombolSalazar = TombolPilihan(115,239,"Salazar",info_salazar)
    #cetak gambar informasi mode
    mode = mode_pilihHero
    pos_mode = (5,317)
    Hero = karakter


def pilihMonster():
    global mode, pos_mode, tombolAposteus, tombolFenrir, \
        cek_pilih_monster, cek_pilih_hero, Monster
    cek_pilih_hero = False
    cek_pilih_monster = True
    #cetak tombol-tombol ke layar
    tombolAposteus = TombolPilihan(115, 317, "Aposteus", info_aposteus)
    tombolFenrir = TombolPilihan(115, 395, "Fenrir", info_fenrir)
    #cetak gambar informasi mode
    mode = mode_pilihMonster
    pos_mode = (5,82)
    Monster = karakter



tombol_back=Button(
    layar,
    36,
    19,
    110,
    50,

    text="BACK",
    font=pygame.font.Font("Assets/font/A Goblin Appears!.otf",20),
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
    font=pygame.font.Font("Assets/font/A Goblin Appears!.otf",20),
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



