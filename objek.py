import pygame
import os
import assetModule
from abc import ABC, abstractmethod


# Abstract class
class Makhluk(ABC):
    def __init__(self, nama):
        self.nama = nama
        self.action = self.prev_action = self.frame = 0
        self.update_time = pygame.time.get_ticks()
        self.onground = False
        self.move_l = self.move_r = self.finish = self.attacking = False

    def obj_collision(self, enemy):
       collide = self.rect.colliderect(enemy.rect)
       return collide

    def floor_collision(self, grounds):
        collide = pygame.sprite.spritecollide(self, grounds, False)
        if collide:
            self.onground = True
            idx = len(collide) - 1
            self.rect.bottom = collide[idx].rect.top
        else:
            self.onground = False

    def update(self, enemy):
        if not self.onground and not self.attacking:
            self.rect.y += 6
        if self.prev_action != self.action:
            self.frame = 0
            self.prev_action = self.action
        else:
            if pygame.time.get_ticks() - self.update_time > 90:
                self.frame = (self.frame + 1) % \
                    len(self.animation[self.action])
                self.update_time = pygame.time.get_ticks()
                if self.attacking:
                    if self.frame == len(self.animation[self.action]) - 1:
                        self.action = 2
                        self.attacking = False
                        self.move_l = True
                        self.frame = 0
                        if self.tipe == 'Hero':
                            self.rect.right = enemy.rect.left
                        else:
                            if self.nama == 'Aposteus':
                                self.rect.y = enemy.rect.y
                            self.rect.left = enemy.rect.right

    @abstractmethod
    def __sub__(self):
        pass

    @abstractmethod
    def serang(self):
        pass

# Parent Class
class Hero(Makhluk):
    def __init__(self, nama, hp, damage, energi=0):
        super().__init__(nama)
        self.__hp = hp
        self.__damage = damage
        self.__energi = energi
        self.turn = 0
        self.tipe = 'Hero'

    def buttonImage(self):
        # Get current Directory
        # Assign gambar tombol
        pass

    def move(self, enemy):
        if self.obj_collision(enemy):
            self.move_r = False
            self.attacking = True
            self.action = 3
        if self.rect.x <= 180 and self.move_l:
            self.move_l = False
            enemy.finish = False
            self.finish = True
            self.action = 0
        if self.move_r:
            self.rect.x += 4
        if self.move_l:
            self.rect.x -= 4

    def serang(self, target):
        self.move_r = True
        self.action = 1
        self.turn += 1

    def skill1(self):
        pass

    def skill2(self):
        pass

    # Famage Getter
    @property
    def damage(self):
        return self.__damage

    # HP Getter
    @property
    def hp(self):
        return self.__hp

    # Energi Getter
    @property
    def energi(self):
        return self.__energi

    # Energi setter 

    @energi.setter
    def energi(self, tambahan):
        self.__energi += tambahan

    # Reducing HP after attacked
    def __sub__(self, amount):
        self.__hp -= amount


class Monster(Makhluk):
    def __init__(self, nama, hp, damage):
        super().__init__(nama)
        self.__hp = hp
        self.__damage = damage
        self.finish = True
        self.tipe = 'Monster'

    def move(self, enemy):
        if self.obj_collision(enemy):
            self.move_r = False
            self.attacking = True
            self.rect.x = 170
            if self.nama == 'Aposteus':
                self.rect.y = 0
            self.action = 3
        if self.rect.x >= 520 and self.move_l:
            self.move_l = False
            enemy.finish = False
            self.finish = True
            self.action = 0
        if self.move_r:
            self.rect.x -= 4
        if self.move_l:
            self.rect.x += 4

    def serang(self, obj):
        obj.turn += 1
        self.move_r = True
        self.action = 1

    def buff(self):
        pass

    # HP Getter
    @property
    def hp(self):
        return self.__hp

    # Damage Getter
    @property
    def damage(self):
        return self.__damage

    # Reducing hp after attacked
    def __sub__(self, amount):
        self.__hp -= amount


class Melee:
    def __init__(self):
        self.atk_range = 10


class Ranged:
    def __init__(self):
        self.atk_range = 70


class Lantai(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            assetModule.game_env, image)).convert()
        self.image = pygame.transform.scale(self.image, (64, 66))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
