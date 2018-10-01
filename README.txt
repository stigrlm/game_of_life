Command line version of popular Game of life implemented in object oriented paradigm,
using numpy array as grid for storing cell objects. Cell objects have implemented
dunder (magic) methods __add__ and __radd__ that allows for counting of alive
cells using numpy sum method.

World is displayed as square grid, however to fulfill the rules of the game, the world
doesn't end on the edge, but is connected to it's opposite side. E.g. cell that lives
in top left corner has neighbour in bottom right corner as well. This simulates
toroid (donut-like) object.

Classes implemented:
InputHandler - handles command lines input to the script
Game - game instance configures world and controls the run of the game
World - contains cells in numpy array and has methods that evaluate each round
Cell - simple class that holds info whether cell is alive or dead

Game can be run using run_game.py script, with option to specify 4 input paramters:
--world_size      how many cells will be on each side (between 10-50, default 30)

--live_density    proportion of alive cells at the beginning (between 0-1. default 0.5)

--rounds_number   for how many rounds the game will run (default 1000)

--run_speed       how many rounds will be evaluated per second (4-30, default 5)
                  if the desired speed is higher than ability of pc to compute
                  rounds, then game will run on max possible speed

example of usage:
run_game.py --world_size 20 --live_density 0.3 --rounds_number 500 --run_speed 10
