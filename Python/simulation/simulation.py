#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyright © Manoel Vilela
#
#

from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
from automaton import Ant, Track
import motion
import pygame
import random
import colors
import grid

FPS = 30


class AntSimulation(object):

    tracks = []
    ants = []

    def __init__(self, width, heigth, fps, n_ants=4):
        self.width = width
        self.heigth = heigth
        self.running = True
        self.fps = fps
        self.n_ants = n_ants
        self.setup()

    def setup(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        self.clock = pygame.time.Clock()
        for _ in range(self.n_ants):
            color = random.choice(colors.VISIBLES)
            self.ants.append(Ant(0, 0, color))

    @property
    def screen_size(self):
        return self.width, self.heigth

    def event_handler(self, event):
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            self.running = False
        elif event.type == QUIT:
            self.running = False

    def random_move(self, entity):
        x, y = random.choice(list(motion.DIRECTIONS.values()))

        if all((0 <= entity.x + x < self.width,
                0 <= entity.y + y < self.heigth)):
            entity.move(x, y)
        else:
            self.random_move(entity)

    def draw_ants(self):
        for ant in self.ants:
            if not any([track.collide(ant) for track in self.tracks]):
                track = Track.footprint(ant)
                track.draw(self.screen)
                self.tracks.append(track)
            self.random_move(ant)
            ant.draw(self.screen)

    def draw_tracks(self):
        for track in self.tracks:
            track.draw(self.screen)

    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                self.event_handler(event)

            self.screen.fill(colors.BLACK)
            self.draw_tracks()
            self.draw_ants()
            pygame.display.flip()
            self.clock.tick(self.fps)

    @classmethod
    def run(cls):
        w, h = grid.GRID_SIZE
        weigth, heigth = w * grid.BLOCKSIZE, h * grid.BLOCKSIZE
        game = cls(weigth, heigth, FPS)
        game.main_loop()
        pygame.quit()
        return game.tracks


if __name__ == '__main__':
    from pprint import pprint
    pprint(sorted(AntSimulation.run(), key=lambda self: (self.x, self.y)))
