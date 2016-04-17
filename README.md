Ant Walking
==========

An ant walking simulation using concepts of randomness at discipline Probability & Statistics

# Python simulation

![simulation](data/python-simulation.gif)


## Design
The python version was wrote using *pygame* for handling the window events, graphics and logic. The coding-style was used Programming Object-Oriented and as more modular as possible. The script whose has the `main-loop` is: [`simulation.py`](Python/simulation/simulation.py).  The other scripts was spited into: 

* [`automaton.py`](Python/simulation/automaton.py)
    - Our specific entities, as Automaton (base), `Ant` and `Track`
* [`base.py`](Python/simulation/base.py)
    - Abstract class called `Entity` designed to inherit from automaton specific classes
* [`colors.py`](Python/simulation/colors.py) 
    - Some colors constants, like WHITE and BLACK
* [`graphics.py`](Python/simulation/graphics.py)
    - 8bit-like graphics for `Ant` and `Track` (the footprint)
* [`grid.py`](Python/simulation/grid.py)
    - about block size and the amount of blocks on screen (the size of matrix)
* [`motion.py`](Python/simulation/motion.py)
    - directions definitions, like `UP`, `DOWN`, `RIGHT` and `LEFT`.
    - All directions definitions are in function of BLOCKSIZE variable in grid.py
* [`main.py`](Python/simulation/main.py)
    - a script helper, only calling the simulation.py `AntSimulation.run()`

## Usage Instrunctions

To execute this you need Python3.x >= (3, 4) or Python2.x >= (2.6).
Beyond that you need too the Pygame library. If you are using Ubuntu, you can type this:

* `sudo apt-get install python-pygame` or `sudo pip install pygame`

If pip was not installed try: `sudo apt-get install python-pip`.

If you are using Windows, you need eternal suffering. Ow, I'm kidding. You can try installing using the pre-compiled lib binaries [`here`](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame) keeping attention with your [python](www.python.org) version.

After that, only execute at terminal in proper directory: `python simulation.py`