#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from num2words import num2words


class Account:
    def __init__(self, surname, number, percent, balance):
        self.surname = surname
        self.number = number
        self.percent = percent
        self.balance = balance
        self.dollars, self.evro = 0, 0

    def read(self):
        surname = input("Введите фамилию владельца счета: ")
        number = int(input("Введите номер счета: "))
        percent = int(input("Введите процент: "))
        balance = int(input("Введите баланс в рублях: "))

        self.__init__(surname, number, percent, balance)

    def popolnenie(self):
        sum_p = int(input("Введите сумму для поплнения: "))
        if sum_p > 0:
            self.balance += sum_p
        else:
            print("Сумма должна быть положительной.")

    def snytie(self):
        sum_s = int(input("Введите сумму, которую хотите списать: "))
        if sum_s > 0 and self.balance > sum_s:
            self.balance -= sum_s
        else:
            print("Сумма должна быть положительной.")

    def percent_interest(self):
        self.balance += round(self.balance * (self.percent / 100))

    def convert_to_dollars(self, kyrs_d):
        if kyrs_d > 0:
            self.dollars = round(self.balance / kyrs_d, 2)
        else:
            print("Неверный курс обмена.")

    def convert_to_euros(self, kyrs_e):
        if kyrs_e > 0:
            self.evro = round(self.balance / kyrs_e, 2)
        else:
            print("Неверный курс обмена.")

    def get_balance_in_words(self):
            return num2words(self.balance, lang='ru').replace('-', ' ')


if __name__ == '__main__':
    a = Account("Кузннецова", "111111", 1, 1000)
    a.read()

    a.popolnenie()
    print("Баланс на счете:", a.balance, "руб.")
    a.percent_interest()
    print("Баланс после начисления процентов:", a.balance)
    a.snytie()
    print("Баланс на счете:", a.balance, "руб.")
    a.convert_to_dollars(99)
    print("Баланс в долларах:", a.dollars, "$")
    a.convert_to_euros(106)
    print("Баланс в евро:", a.evro, "€")
    print("Баланс прописью:", a.get_balance_in_words())
