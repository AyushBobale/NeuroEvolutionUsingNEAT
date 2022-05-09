import os
from simulation import Simulation
from organism import Organsim
import neat
import pygame

def eval_genome(genomes, config):
    sim_instance    = Simulation(1800, 400, 60)
    networks = []
    for genomeid, genome in genomes:
        network         = neat.nn.FeedForwardNetwork.create(genome, config)
        networks.append(network)
    fitness = sim_instance.trainAIBootleg(networks)
    for i, (genomeid, genome) in enumerate(genomes):
        genome.fitness = fitness[i]

    

def runNeat(config):
    pop = neat.Checkpointer.restore_checkpoint('neat-checkpoint-81')
    #pop = neat.Population(config)
    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    pop.add_reporter(neat.Checkpointer(1))
    pop.run(eval_genome, 200)


if __name__ == "__main__":
    LOCALDIR = os.path.dirname(__file__)
    config_path = os.path.join(LOCALDIR, "config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    runNeat(config)
    """
    To Do :
    ----------------------------------------------------
    UI overhaul
    More custom organism
    Optimize how walking is done
    Color organism based on network
    scrollabel background
    """
