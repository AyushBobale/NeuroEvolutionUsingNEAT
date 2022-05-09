# NeuroEvolutionUsingNEAT

A python project created to train creatures how to walk as far as possible in a single direction.

The 2D world is simulated using the pymunk library of python.

The genetic algorithm is implemented using the python's NEAT library.

## Sample Organism
![Simulation Screen Shot](https://github.com/AyushBobale/NeuroEvolutionUsingNEAT/blob/main/imgs/mainss.PNG?raw=true "Sample Organism")

## How to run

``` bash
git clone https://github.com/AyushBobale/NeuroEvolutionUsingNEAT
cd NeuroEvolutionUsingNEAT
pip install pymunk
pip install pygame
pip install neat-python
python simulation.py 
```
## Starting gens [Generation 1 and onwards]
![Simulation Screen Shot](https://github.com/AyushBobale/NeuroEvolutionUsingNEAT/blob/main/imgs/startgen.gif?raw=true "Generation 1 and onwards")

## Late gens [Generation 81 and onwards]
![Simulation Screen Shot](https://github.com/AyushBobale/NeuroEvolutionUsingNEAT/blob/main/imgs/endgen.gif?raw=true "Generation 81 and onwards")


* For Blue leg
    * A - Left
    * S - Down
    * D - Right
    * W - Up

* For Blue leg
    * LeftArrow - Left
    * DownArrow - Down
    * RightArrow - Right
    * UpArrow - Up