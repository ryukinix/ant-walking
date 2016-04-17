#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

import grid

DIRECTIONS = {
    "UP": (0, -grid.BLOCKSIZE),
    "LEFT": (-grid.BLOCKSIZE, 0),
    "RIGHT": (grid.BLOCKSIZE, 0),
    "DOWN": (0, grid.BLOCKSIZE)
}

