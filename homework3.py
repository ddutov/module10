# -*- coding: utf-8 -*-
from threading import Thread
import threading
import time


class BankAccount(Thread):

    def __init__(self, account=1000, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.account = account
        self.lock = threading.Lock()  # используем класс Lock из модуля threading для блокировки доступа к общему ресурсу.

    def deposit(self, amount):
        with self.lock:  # используем with (lock object): в начале каждого метода, чтобы использовать блокировку
            self.account += amount
            print(f'Deposit 100, new balance is {self.account} coins')

    def withdraw(self, amount):
        with self.lock:  # используем with (lock object): в начале каждого метода, чтобы использовать блокировку
            self.account -= amount
            print(f'Whithdrew 150, new balance is {self.account} coins')


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


balance = BankAccount(1000)  # стартовый баланс на счете
deposit_thread = threading.Thread(target=deposit_task, args=(balance, 100))  # создание двух потоков, один для пополнения счета,
withdraw_thread = threading.Thread(target=withdraw_task, args=(balance, 150))  # другой для снятия денег.
deposit_thread.start()  # запуск потока пополнения
withdraw_thread.start()  # запуск потока снятия
deposit_thread.join()
withdraw_thread.join()
