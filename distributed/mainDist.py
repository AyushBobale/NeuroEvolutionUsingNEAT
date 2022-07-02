import neat
import os
import time
import pickle
import ray

"""
========================================================================================

Make a class state [must be serializeable]
Do functional progrming approach 
just make the merhod remote which returns the fitness 
**
https://dev.to/yuikoito/using-opencv-developed-a-web-app-to-convert-images-to-manga-style-23p0 
image conversion


========================================================================================
"""

@ray.remote
def trainAI(network):
    inputs =  (1,1)
    op = network.activate(inputs)
    time.sleep(0.25)
    return op[0]


def eval_genome(genomes, config):
    networks = []

    for genomeid, genome in genomes:
        network         = neat.nn.FeedForwardNetwork.create(genome, config)
        networks.append(network)
    
    futs = [trainAI.remote(network) for network in networks]
    fitness = [ray.get(fut) for fut in futs]

    print(len(fitness), len(futs), len(networks))

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
    ray.init()
    LOCALDIR = os.path.dirname(__file__)
    config_path = os.path.join(LOCALDIR, "config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    starttime = time.time()
    runNeat(config)
    print(time.time() -starttime)