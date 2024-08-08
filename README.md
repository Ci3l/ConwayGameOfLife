# Conway's Game of Life

![](assets/LifeGame.gif)

## Description

**Conway's [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)** is a classic cellular automaton simulation, implemented for NumWorks calculators (N 100 and N 110) using Python and the [Kandinsky package](https://www.numworks.com/fr/ressources/python/activites/kandinsky/). This project was created to enhance my skills in handling matrices in Python and to develop a functional script for my NumWorks calculator.

## Features

- **Matrix-Based Simulation:** Uses a matrix to represent the game grid, with cells evolving based on Conway's rules.
- **Adaptive Display:** Dynamically adjusts the visualization to fit the screen of the NumWorks calculator.
- **Customizable Parameters:** Allows for different grid sizes and generation counts.

## Technologies

- **Programming Language:** Python
- **Libraries Used:** Kandinsky package for graphics on NumWorks calculators

## Usage

### NumWorks Calculator

To run the game on a NumWorks calculator, you can use the built-in emulator or install the script directly on your calculator. The project can be tested using the integrated emulator on the NumWorks website [here](https://my.numworks.com/python/ciel/conway). The basic command to start the simulation is:

```python
start(generation, length, width)
```
You can specify three grid sizes: 16x10, 32x20, and 40x25. If you don't specify parameters, default values will be used:
```python
start()
```
### PC Version
A PC version of the project is available in the pc vers directory for those who prefer to test it on a computer.

### Demo
To see the game in action, visit the NumWorks website and test the project on the integrated emulator [here](https://my.numworks.com/python/ciel/conway). Click on the 'play' icon to start the simulation. Alternatively, use the PC version available in the 'pc vers' directory.

### Participation
I welcome feedback and contributions to this project. Feel free to reach out via [email](mailto:poire.erwan2005@gmail.com), submit a pull request, or open an issue to share your thoughts or suggestions.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

