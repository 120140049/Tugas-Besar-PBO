from abc import ABC, abstractmethod


class Makhluk(ABC):
    def __init__(self, nama, hp, damage):
        self.nama = nama
        self.__hp = hp
        self.__damage = damage

    def __sub__(self, obj):
        self.__hp -= obj.__hp

    @property
    def hp(self):
        return self.__hp

    @abstractmethod
    def serang(self):
        pass


class Hero(Makhluk):
    def __init__(self, nama, hp, damage):
        super().__init__(nama, hp, damage)
        self.__energi = 0

    @property
    def energi(self):
        return self.__energi

    @energi.setter
    def energi(self, tambahan):
        self.__energi += tambahan

    def serang(self):
        pass

    def skill1(self):
        pass

    def skill2(self):
        pass

class Monster(Makhluk):
    def __init__(self, nama, hp, damage):
        super().__init__(nama, hp, damage)

    def serang(self):
        pass

    def buff(self):
        pass

class Hero1(Hero):
    def __init__(self, nama, hp, damage):
        super().__init__(nama, hp, damage)

    def skill1(self):
        pass

    def skill2(self):
        pass

class Hero2(Hero):
    def __init__(self, nama, hp, damage):
        super().__init__(nama, hp, damage)

    def skill1(self):
        pass

    def skill2(self):
        pass

class Hero3(Hero):
    def __init__(self, nama, hp, damage):
        super().__init__(nama, hp, damage)

    def skill1(self):
        pass

    def skill2(self):
        pass

class Monster1(Monster):
    def __init__(self, nama, hp, damage):
        super().__init__(nama, hp, damage)

    def buff(self):
        pass

class Monster2(Monster):
    def __init__(self, nama, hp, damage):
        super().__init__(nama, hp, damage)

    def buff(self):
        pass
