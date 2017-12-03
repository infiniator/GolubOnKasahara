from src.comparator import compareChromosomes
from src.genetic_algorithm import *
from src.chromosome import *
import numpy as np
from time import time
import matplotlib.pyplot as plt


def main(file, size, iter, cross, mutate):
    # populationSize = int(input('Enter Population Size: '))
    init = Chromosome(file)
    population = initialisation(size)
    # numIterations = int(input('Enter number of iterations: '))
    myPlot = []
    for i in range(0, iter):
        # print(i)
        children = []
        while len(children) < len(population):
            parent1 = selection(population, randrange(2, 5))
            parent2 = selection(population, randrange(2, 5))
            flag = np.random.choice([False, True], p=[cross, mutate])
            if flag:
                child1 = mutation(parent1)
                child2 = mutation(parent2)
            else:
                child1, child2 = crossover(parent1, parent2)
            child1.calculateFitness()
            child2.calculateFitness()
            children.append(child1)
            children.append(child2)
        population = population + children
        population.sort(key=cmp_to_key(compareChromosomes))
        population = population[:size]
        myPlot.append(np.mean([k.fitness for k in population]))
        # myPlot.append(population[0].fitness)
    print(population[0].fitness)
    # print(population[len(population) - 1].fitness)
    plt.plot(myPlot)
    plt.xlabel('Number of iterations')
    plt.ylabel('Fitness of the population')
    s = 'file-' + str(file) + '_' + str(size) + '-chr_' + str(
        iter) + '-iter_' + str(cross) + '_' + str(mutate) + '.svg'
    plt.savefig(s, format='svg')
    plt.gcf().clear()
    Chromosome.initialized = False


start_time = time()
for i in range(0, 10):
    main(i, 20, 1000, 0.99, 0.01)
print("--- %s seconds ---" % (time() - start_time))
