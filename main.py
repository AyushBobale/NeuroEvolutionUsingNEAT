import os
from simulation import Simulation
from simulationNoBounds import SimulationNoBounds
from organism import Organsim
import neat
import pickle
import pygame

"""

"""

def eval_genome(genomes, config):
    #16:9 aspect rations work properly
    #last argument is delta time dont change unless necessary
    #can be left as None [only for fps 60]
    #3rd argument is fps
    sim_instance    = SimulationNoBounds(1270, 720, 100, 1/60)
    networks = []
    for genomeid, genome in genomes:
        network         = neat.nn.FeedForwardNetwork.create(genome, config)
        networks.append(network)
    fitness = sim_instance.trainAI(networks, 600) #Simultion No bounds train ai function requires no of frames the gen to be trained
    for i, (genomeid, genome) in enumerate(genomes):
        genome.fitness = fitness[i]


def testAI(config):
    with open(r"C:\Users\Ayush\Documents\Documents folder\NeuroEvolutionUsingNEAT\checkpoint-backup\best_pickle720pbipedal99gen","rb") as f:
        winner = pickle.load(f)
    sim_instance    = SimulationNoBounds(1270, 720, 60)
    networks = []
    network         = neat.nn.FeedForwardNetwork.create(winner, config)
    networks.append(network)
    sim_instance.trainAI(networks, 3000000)

def runNeat(config):
    #pop = neat.Checkpointer.restore_checkpoint('neat-checkpoint1')
    pop = neat.Population(config)
    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    pop.add_reporter(neat.Checkpointer(1))

    winner = pop.run(eval_genome, 1)
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
