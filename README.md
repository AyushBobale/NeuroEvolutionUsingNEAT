# NeuroEvolutionUsingNEAT

A python project created to train creatures how to walk as far as possible in a single direction.

The 2D world is simulated using the pymunk library of python.

The genetic algorithm is implemented using the python's NEAT library.

## New Scrollable Environment
![ScrollabelEnvironment](https://github.com/AyushBobale/NeuroEvolutionUsingNEAT/blob/main/imgs/scrollable.gif?raw=true)
### To Move camera
* Left Arrow key
* Right Arrow Key

## New Organism Bipedal
### For initial generations 
![Starting Generation](https://github.com/AyushBobale/NeuroEvolutionUsingNEAT/blob/main/imgs/bipedalinit.gif?raw=true)

### For later generations [Not what I expected to be the behaviour even with a custom modified fitness function]
![Ending Generation](https://github.com/AyushBobale/NeuroEvolutionUsingNEAT/blob/main/imgs/bipedallater.gif?raw=true)



### Best genome pickling and loading for test replays added


## How to run

``` bash
git clone https://github.com/AyushBobale/NeuroEvolutionUsingNEAT
cd NeuroEvolutionUsingNEAT
pip install pymunk
pip install pygame
pip install neat-python
python main.py 
```
---
# Previous Work
## Sample Organism
![Simulation Screen Shot](https://github.com/AyushBobale/NeuroEvolutionUsingNEAT/blob/main/imgs/mainss.PNG?raw=true "Sample Organism")


## For initial generations [Generation 1]
![Starting Generation](https://github.com/AyushBobale/NeuroEvolutionUsingNEAT/blob/main/imgs/startgen.gif?raw=true "Generation 1")

## For later generations [Generation 81]
![Ending Generation](https://github.com/AyushBobale/NeuroEvolutionUsingNEAT/blob/main/imgs/endgen.gif?raw=true "Generation 81")


