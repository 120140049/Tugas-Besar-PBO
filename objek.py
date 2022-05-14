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
        self.onground = self.onfloor = self.death = self.die = False
        self.move_l = self.move_r = self.finish = self.attacking = False

    def obj_collision(self, enemy):
       collide = self.rect.colliderect(enemy.rect)
       return collide

    def floor_collision(self, grounds):
        collide = pygame.sprite.spritecollide(self, grounds, False)
        if collide:
            self.onground = True
            self.onfloor = True
            idx = len(collide) - 1
            self.rect.bottom = collide[idx].rect.top
        else:
            self.onground = False

    def update(self, enemy):
        if self.hp <= 0:
            self.death = True
        if enemy.hp <= 0:
            enemy.death = True
        if not self.onground and not self.attacking:
            self.rect.y += 3
        if self.prev_action != self.action:
            self.frame = 0
            self.prev_action = self.action
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
                    enemy - self.damage
                    self + 1
            if self.tipe == 'Hero' and self.action == 4:
                if self.frame == len(self.animation[self.action]) - 1:
                    self.action = 0
                    self.frame = 0
                    self.die = True

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
        self.__damage = 13123123
        self.__energi = energi
        self.tipe = 'Hero'
        self.turn = 0
        self.dead_img = None
        self.skilled = False

    def move(self, enemy):
        if not self.death:
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
                self.rect.x += 5
            if self.move_l:
                self.rect.x -= 5
        else:
            self.action = 4        

    def serang(self):
        self.move_r = True
        self.action = 1
        self.turn += 1

    def skill1(self):
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

    @energi.setter
    def energi(self, tambahan):
        self.__energi -= tambahan

    # Reducing HP after attacked
    def __sub__(self, amount):
        self.__hp -= amount

    def __add__(self, amount):
        if self.__energi < 5:
            self.__energi += amount


class Monster(Makhluk):
    def __init__(self, nama, hp, damage):
        super().__init__(nama)
        self.__hp = hp
        self.__damage = 12312312
        self.__buffmeter = 0
        self.finish = True
        self.tipe = 'Monster'
        self.buffed = False
        self.buff_time = 0

    def move(self, enemy):
        if self.death:
            if enemy.action == 0:
                self.action = 2
            if self.rect.x >= 896:
                self.action = 0
                self.die = True
            elif enemy.action == 0:
                self.rect.x += 6
        else:
            if self.obj_collision(enemy):
                self.move_r = False
                self.attacking = True
                self.rect.x = 150
                if self.nama == 'Aposteus':
                    self.rect.y = 0
                self.action = 3
            if self.rect.x >= 520 and self.move_l:
                self.move_l = False
                self.action = 0
                if self.buffed:
                    self.buff()
                else:
                    self.finish = True
                    enemy.finish = False
            if self.move_r:
                self.rect.x -= 6
            if self.move_l:
                self.rect.x += 6

    def serang(self, obj):
        self.move_r = True
        self.action = 1
        obj.turn += 1

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

    @property
    def buffmeter(self):
        return self.__buffmeter

    @hp.setter
    def hp(self, amount):
        self.__hp += amount

    @damage.setter
    def damage(self, amount):
        self.__damage += amount

    @buffmeter.setter
    def buffmeter(self, amount):
        self.__buffmeter = amount
    # Reducing hp after attacked
    def __sub__(self, amount):
        self.__hp -= amount

    def __add__(self, amount):
        if self.__buffmeter < 4:
            self.__buffmeter += 1


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
