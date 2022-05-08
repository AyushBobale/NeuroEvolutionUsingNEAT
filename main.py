import os
from simulation import Simulation
from organism import Organsim
import neat
import pygame

def run(width, height, fps):
    sim_instance = Simulation(1980, 1080, 60)
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

def eval_genome(genomes, config):
    for genomeid, genome in genomes:
        genome.fitness = 1
    pass

def runNeat(config):
    #pop = neat.Checkpointer.restore_checkpoint('neat-checkpoint1')
    pop = neat.Population(config)
    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    pop.add_reporter(neat.Checkpointer(1))

    pop.run(eval_genome, 50)


if __name__ == "__main__":
    LOCALDIR = os.path.dirname(__file__)
    config_path = os.path.join(LOCALDIR, "config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    #run(1270, 720, 60)
    runNeat(config)
