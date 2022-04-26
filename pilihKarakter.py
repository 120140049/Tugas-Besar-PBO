# #baru bikin aja
# #ntar ajala kerjainnya


import pygame
import sys
import pygame_widgets
from pygame_widgets.button import Button


pygame.init()
layar = pygame.display.set_mode((896,504))
main_font=pygame.font.SysFont("Times",65)
pos_info=(530,82)
dimensi_ava=(110,70)
info_karakter=pygame.image.load('img/pilihKarakter/unknownchar.png')
klik=None

class TombolPilihan():
    pilihan_karakter=[]
    def __init__(self, gambar_avatar, pos_x, pos_y, nama_karakter,gambar_info):
        self.nama_karakter=nama_karakter
        self.gambar_avatar=gambar_avatar
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
            fontSize=65,
            textHAlign=('left'),
            # font=("Times",65),
            inactiveColour=(173,217,201),
            hoverColour=(255, 206, 160),
            onClick=lambda: update(self) #muncullah masalah baru
            )
        TombolPilihan.pilihan_karakter.append(tombol)

def update (karakter):
    global info_karakter,klik
    klik=True
    info_karakter=karakter.gambar_info

ava=pygame.image.load('img/pilihKarakter/test_ava.png')
ava=pygame.transform.scale(ava,dimensi_ava)    
background=pygame.image.load('img/pilihKarakter/bg_pilihKarakter.jpeg')
background=pygame.transform.scale(background,(896,504))    

#gambar info
info_alectrona=pygame.image.load('img/pilihKarakter/infoAlectrona.png')
info_nipalto=pygame.image.load('img/pilihKarakter/infoNipalto.png')
info_salazar=pygame.image.load('img/pilihKarakter/infoSalazar.png')
info_aposteus=pygame.image.load('img/pilihKarakter/infoAposteus.png')
info_fenrir=pygame.image.load('img/pilihKarakter/infoFenrir.png')


tombolAlectrona=TombolPilihan(ava,115,82,"Alectrona",info_alectrona)
tombolNipalto=TombolPilihan(ava,115,160,"Nipalto",info_nipalto)
tombolSalazar=TombolPilihan(ava,115,239,"Salazar",info_salazar)
tombolAposteus=TombolPilihan(ava,115,317,"Aposteus",info_aposteus)
tombolFenrir=TombolPilihan(ava,115,395,"Fenrir",info_fenrir)
#nanti tambahin lagi atribut warna_respon buat kustomisasi warna respon tiap karakter
tombol_back=Button(
    layar,
    36,
    19,
    110,
    50,

    text="BACK",
    fontSize=30,
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
    layar.blit(ava,(5,82))
    #ceritanya ini hero 2
    layar.blit(ava,(5,160))
    #ceritanya ini hero 3
    layar.blit(ava,(5,239))
    #ceritanya ini hero 4
    layar.blit(ava,(5,317))
    #ceritanya ini hero 5
    layar.blit(ava,(5,395))

    if klik:
        #ini nanti buat gambar info_karakter
        layar.blit(info_karakter,(530,82))

    #taro paling bawah, ini buat update semua perubahan
    pygame.display.update()



