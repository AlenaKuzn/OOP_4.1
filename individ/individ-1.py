#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Time:
    def __init__(self, hours, minutes):
        if not isinstance(hours, int) or not isinstance(minutes, int):
            raise ValueError()
        if hours < 0 or minutes < 0:
            raise ValueError()
        self.first = hours
        self.second = minutes

    def read(self):
        hours = int(input("Введите часы: "))
        minutes = int(input("Введите минуты: "))
        self.__init__(hours, minutes)

    def display(self):
        print(self.first * 60 + self.second)


if __name__ == '__main__':
    t = Time(1, 1)
    t.display()

    t.read()
    t.display()
