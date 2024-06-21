# -*- coding: utf-8 -*-

"""Напишите программу, которая создает два потока.
Первый поток должен выводить числа от 1 до 10 с интервалом в 1 секунду.
Второй поток должен выводить буквы от 'a' до 'j' с тем же интервалом.
Оба потока должны работать параллельно."""

import time
from threading import Thread


def printing(var):
    for i in range(len(var)):
        print(var[i])
        time.sleep(1)


first_var = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
second_var = tuple('abcdefghij')
thread = Thread(target=printing, args=(first_var, ))
thread.start()
# time.sleep(0.5)  # раскомментировать строку если при выводе потоков происходит склеивание чисел и строк
thread = Thread(target=printing, args=(second_var, ))
thread.start()
