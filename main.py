import os
from simulation import Simulation
from simulationNoBounds import SimulationNoBounds
from organism import Organsim
import neat
import pickle
import pygame

"""

"""

#VARS 
#================================================================================================================
WIDTH               = 1270
HEIGHT              = 720
FORCE_MULTIPLIER    = 2.5
TRAIN_FPS           = 120
TEST_FPS            = 60
DT                  = 1/60
TRAIN_FRAMES        = 600
TEST_FRAMES         = 300000
PICKLE_PATH         = r"checkpoint\best_pickle720pHuman49genIC"
#================================================================================================================


def eval_genome(genomes, config):
    #16:9 aspect rations work properly
    #last argument is delta time dont change unless necessary
    #can be left as None [only for fps 60]
    #3rd argument is fps
    sim_instance    = SimulationNoBounds(WIDTH, HEIGHT, TRAIN_FPS, DT)
    networks = []
    for genomeid, genome in genomes:
        network         = neat.nn.FeedForwardNetwork.create(genome, config)
        networks.append(network)
    fitness = sim_instance.trainAI(networks, TRAIN_FRAMES, FORCE_MULTIPLIER) #Simultion No bounds train ai function requires no of frames the gen to be trained
    for i, (genomeid, genome) in enumerate(genomes):
        genome.fitness = fitness[i]


def testAI(config):
    with open(PICKLE_PATH,"rb") as f:
        winner = pickle.load(f)
    sim_instance    = SimulationNoBounds(WIDTH, HEIGHT, TEST_FPS)
    networks = []
    network         = neat.nn.FeedForwardNetwork.create(winner, config)
    networks.append(network)
    sim_instance.trainAI(networks, TEST_FRAMES,FORCE_MULTIPLIER)

def runNeat(config):
    #pop = neat.Checkpointer.restore_checkpoint('neat-checkpoint1')
    pop = neat.Population(config)
    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    pop.add_reporter(neat.Checkpointer(1))

    winner = pop.run(eval_genome, 50)
    with open("best_pickle", "wb") as f:
        pickle.dump(winner, f)


if __name__ == "__main__":
    LOCALDIR = os.path.dirname(__file__)
    config_path = os.path.join(LOCALDIR, "config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    #runNeat(config)
    testAI(config)
