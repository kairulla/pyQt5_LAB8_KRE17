#!/usr/bin/env python3
# coding=utf-8
import math


class TaskSolver(object):

    def __init__(self, K):
        self.K = K.copy()
        self.Y = []

    def getReshenie(self):
        for count, i in enumerate(self.K):
            if (i < 0):
                sum = 0
                for s in range(count):
                    sum = sum + self.K[s]
                radian = math.radians(sum)
                y = math.sin(radian) / i
                self.Y.append(y)
            if (i == 0):
                koren = math.sqrt(i)
                y = math.cos(koren) ** 2
                self.Y.append(y)
            if (i > 0):
                proizv = 1
                for pr in range(count):
                    proizv = proizv * self.K[pr]

                item = self.K[count - 1]
                radian1 = math.radians(item)
                y = proizv - math.tan(radian1)
                self.Y.append(y)
        return self.Y
