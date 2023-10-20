#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Time:
    def __init__(self, hours, minutes):
        self.hous = hours
        self.min = minutes

    def read(self):
        hours = int(input("Введите часы: "))
        minutes = int(input("Введите минуты: "))
        self.__init__(hours, minutes)

    def display(self):
        print(self.hous * 60 + self.min)


if __name__ == '__main__':
    t = Time(1, 1)
    t.display()

    t.read()
    t.display()
