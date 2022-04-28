# #baru bikin aja
# #ntar ajala kerjainnya


import pygame
import sys
import pygame_widgets
from pygame_widgets.button import Button
import os

CWD=os.getcwd()
pathfile=os.path.join(CWD, "img/pilihKarakter")
pygame.init()
layar = pygame.display.set_mode((896,504))
main_font=pygame.font.Font("font/A Goblin Appears!.otf",35)
pos_info=(530,82)
dimensi_ava=(110,70)
info_karakter=pygame.image.load(os.path.join(pathfile,'unknownchar.png'))
klik=None

class TombolPilihan():
    pilihan_karakter=[]
    def __init__(self, pos_x, pos_y, nama_karakter,gambar_info):
        self.nama_karakter=nama_karakter
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.gambar_info=gambar_info
        TombolPilihan.generate(self)
        # self.rect.center=[pos_x,pos_y]
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
            onClick=lambda: update(self) #muncullah masalah baru
            )
        TombolPilihan.pilihan_karakter.append(tombol)

def update (karakter):
    global info_karakter,klik
    klik=True
    info_karakter=karakter.gambar_info

avaAlectrona=pygame.image.load(os.path.join(pathfile,'avaAlectrona.png'))
avaNipalto=pygame.image.load(os.path.join(pathfile,'avaNipalto.png'))
avaSalazar=pygame.image.load(os.path.join(pathfile,'avaSalazar.png'))
avaAposteus=pygame.image.load(os.path.join(pathfile,'avaAposteus.png'))
avaFenrir=pygame.image.load(os.path.join(pathfile,'avaFenrir.png'))
   
background=pygame.image.load(os.path.join(pathfile,'bg_pilihKarakter.jpeg'))
background=pygame.transform.scale(background,(896,504))    

#gambar info
info_alectrona=pygame.image.load(os.path.join(pathfile,'infoAlectrona.png'))
info_nipalto=pygame.image.load(os.path.join(pathfile,'infoNipalto.png'))
info_salazar=pygame.image.load(os.path.join(pathfile,'infoSalazar.png'))
info_aposteus=pygame.image.load(os.path.join(pathfile,'infoAposteus.png'))
info_fenrir=pygame.image.load(os.path.join(pathfile,'infoFenrir.png'))


tombolAlectrona=TombolPilihan(115,82,"Alectrona",info_alectrona)
tombolNipalto=TombolPilihan(115,160,"Nipalto",info_nipalto)
tombolSalazar=TombolPilihan(115,239,"Salazar",info_salazar)
tombolAposteus=TombolPilihan(115,317,"Aposteus",info_aposteus)
tombolFenrir=TombolPilihan(115,395,"Fenrir",info_fenrir)
#nanti tambahin lagi atribut warna_respon buat kustomisasi warna respon tiap karakter
tombol_back=Button(
    layar,
    36,
    19,
    110,
    50,

    text="BACK",
    fontSize=30,
    font=pygame.font.Font("font/A Goblin Appears!.otf",20),
    textColour='white',
    inactiveColour=(99, 113, 115),
    hoverColour=(217, 17, 17),
    onClick=lambda: print('Tombol back')
)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
    layar.fill("white")
    layar.blit(background,(0,0))
    layar.blit(info_karakter,(530,82))
    pygame_widgets.update(event)
    #ceritanya ini hero 1
    layar.blit(avaAlectrona,(5,82))
    #ceritanya ini hero 2
    layar.blit(avaNipalto,(5,160))
    #ceritanya ini hero 3
    layar.blit(avaSalazar,(5,239))
    #ceritanya ini hero 4
    layar.blit(avaAposteus,(5,317))
    #ceritanya ini hero 5
    layar.blit(avaFenrir,(5,395))

    if klik:
        #ini nanti buat gambar info_karakter
        layar.blit(info_karakter,(530,82))

    #taro paling bawah, ini buat update semua perubahan
    pygame.display.update()



