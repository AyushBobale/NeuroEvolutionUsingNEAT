import os
from simulation import Simulation
from organism import Organsim
import neat
import pygame
"""
def run(sim_instance):
    running  = True
    sim_instance.createBoundaries()
    new_org = Organsim(sim_instance.space, sim_instance.width, sim_instance.height)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            new_org.sMove(event, force_multiplier=0.3) #very high force multiplier will break the simulation
        
        sim_instance.fpsCheck()
        sim_instance.draw()
        sim_instance.step()
    pygame.quit()
"""

def eval_genome(genomes, config):
    sim_instance    = Simulation(1800, 720, 60)
    networks = []
    for genomeid, genome in genomes:
        network         = neat.nn.FeedForwardNetwork.create(genome, config)
        networks.append(network)
        #genome.fitness  = 1
    fitness = sim_instance.trainAIBootleg(networks)
    print(fitness)
    for i, (genomeid, genome) in enumerate(genomes):
        genome.fitness = fitness[i]

    

def runNeat(config):
    #pop = neat.Checkpointer.restore_checkpoint('neat-checkpoint1')
    pop = neat.Population(config)
    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    pop.add_reporter(neat.Checkpointer(1))

    pop.run(eval_genome, 100)


if __name__ == "__main__":
    LOCALDIR = os.path.dirname(__file__)
    config_path = os.path.join(LOCALDIR, "config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    #run(1270, 720, 60)
    runNeat(config)
