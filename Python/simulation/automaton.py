#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyright © Manoel Vilela
#
#

from pygame import Rect
from base import Entity
import pygame
import graphics
import colors
import grid


class Automaton(Entity):

    @property
    def position(self):
        return (self.x, self.y)

    @property
    def rect(self):
        return Rect(self.x, self.y, self.blocksize, self.blocksize)

    @property
    def graphics(self):
        rects = []
        width, heigth = self.sub_blocksizes
        for y, line in enumerate(self._graphics):
            for x, point in enumerate(line):
                if point != '.':
                    left = x * width + self.x
                    top = y * heigth + self.y
                    rects.append(Rect(left, top, width, heigth))

        return rects

    def collide(self, entity):
        return self.rect.colliderect(entity.rect)

    @property
    def sub_blocksizes(self):
        return (self.blocksize // len(self._graphics[0]),
                self.blocksize // len(self._graphics))

    def move(self, x=0, y=0):
        self.x += x
        self.y += y

    def draw(self, screen):
        for pixel in self.graphics:
            pygame.draw.rect(screen, self.color, pixel)


class Ant(Automaton):

    def __init__(self, x, y, color=colors.RED, blocksize=grid.BLOCKSIZE):
        super().__init__(x, y, color, graphics.ant, blocksize)


class Track(Automaton):

    def __init__(self, x, y, color=colors.BLUE, blocksize=grid.BLOCKSIZE):
        super().__init__(x, y, color, graphics.track, blocksize)
        self.count = 1

    def __repr__(self):
        return "Track{} | count: {}".format(self.position, self.count)

    @classmethod
    def footprint(cls, ant):
        return cls(ant.x, ant.y, ant.color, ant.blocksize)

    def collide(self, entity):
        collided = super().collide(entity)
        if collided:
            self.mutate_color(entity.color)
            self.count += 1

        return collided

    def mutate_color(self, color):
        self.color = color


__all__ = [
    "Ant",
    "Track"
]
