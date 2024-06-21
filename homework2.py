# -*- coding: utf-8 -*-
"""Каждый рыцарь должен иметь имя (name) и умение(skill) - способность ослабить вражеское войско на skill-человек в день."""

import time
from threading import Thread


class Knight(Thread):

    def __init__(self, name, skill, army=100, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.skill = skill
        self.army = army
        self.day = 0

    def run(self):
        self.day = 0
        while self.army > 0:
            self.day += 1
            self.army -= self.skill
            if self.army < 0:
                self.army = 0
            print(f'Sir {self.name}, сражается {self.day} день(дня)..., осталось {self.army} войнов.')
            time.sleep(1)


enemies = int(input('Введите количество войнов в армии врага: '))
knight1 = Knight("Sir Lancelot", 10, army=enemies)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20, army=enemies)  # Высокий уровень умения
print(f'{knight1.name}, на нас напало {enemies} войнов!!!')
print(f'{knight2.name}, на нас напало {enemies} войнов!!!')
print('-' * 10, 'Начинается смертельная битва!!! ', '-' * 10)
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print('-' * 10, 'Вражеская армия разбита!!! ', '-' * 10)
print(f'{knight1.name}, одержал победу спустя {knight1.day} дней!!!')
print(f'{knight2.name}, одержал победу спустя {knight2.day} дней!!!')
