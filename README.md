# Conway's Game of Life

Conway's Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It consists of a grid of cells that evolve through a series of generations based on a simple set of rules. Despite its simplicity, it can generate complex patterns and behaviors.

This project is an implementation of Conway's Game of Life. The grid evolves over time, with each cell being either "alive" or "dead," depending on its neighbors. The rules governing the evolution of the grid are:

- Any live cell with fewer than two live neighbors dies (underpopulation).
- Any live cell with two or three live neighbors survives to the next generation.
- Any live cell with more than three live neighbors dies (overpopulation).
- Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

Change initial conditions in `map.lif` file. 
