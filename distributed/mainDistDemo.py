import neat
import os
import time
import pickle

class SimulationDistributed:
    def __init__(self):
        self.value = "test"
    
def trainAI(network):
    time.sleep(0.1)
    return 1

#whatever this is doing should be distributed
def eval_genome(genomes, config):
    sim_instance = SimulationDistributed()
    networks = []
    for genomeid, genome in genomes:
        network         = neat.nn.FeedForwardNetwork.create(genome, config)
        networks.append(network)
    
    fitness_future = [trainAI(network) for network in networks]
    fitness = fitness_future
    for i, (genomeid, genome) in enumerate(genomes):
        genome.fitness = fitness[i]
    

def runNeat(config):
    #pop = neat.Checkpointer.restore_checkpoint('neat-checkpoint1')
    pop = neat.Population(config)
    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    pop.add_reporter(neat.Checkpointer(10))

    winner = pop.run(eval_genome, 5)
    with open("best_pickle_dist", "wb") as f:
        pickle.dump(winner, f)


if __name__ =="__main__":
    LOCALDIR = os.path.dirname(__file__)
    config_path = os.path.join(LOCALDIR, "config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    starttime = time.time()
    runNeat(config)
    print(time.time() -starttime)