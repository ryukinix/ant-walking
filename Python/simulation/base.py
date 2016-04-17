#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyright © Manoel Vilela
#
#

from abc import ABCMeta, abstractproperty, abstractmethod


class Entity(metaclass=ABCMeta):

    def __init__(self, x, y, color, graphics, blocksize=8):
        self.x = x
        self.y = y
        self.color = color
        self.blocksize = blocksize
        self._graphics = graphics

    @abstractproperty
    def position(self):
        """Get the positions of entity"""
        pass

    @abstractproperty
    def rect(self):
        """The rectangule of actual position"""
        pass

    @abstractproperty
    def graphics(self):
        """An collection of rects in the correct order"""
        pass

    @abstractmethod
    def move(self, x=0, y=0):
        """Move the player"""
        pass

    @abstractmethod
    def draw(self, screen):
        """Draw the entity on the screen"""
        pass
