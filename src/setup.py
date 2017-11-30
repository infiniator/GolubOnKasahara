from src.comparator import compareChromosomes
from src.genetic_algorithm import *
from src.chromosome import *
import numpy.random as np
from time import time
import matplotlib.pyplot as plt

start_time = time()
# populationSize = int(input('Enter Population Size: '))
population = initialisation(100)
# numIterations = int(input('Enter number of iterations: '))
myPlot = []
for i in range(0, 500):
    print(i)
    children = []
    while len(children) < len(population):
        parent1 = selection(population, randrange(2, 5))
        parent2 = selection(population, randrange(2, 5))
        flag = np.choice([False, True], p=[0.95, 0.05])
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
    population = population[:10]
    myPlot.append(population[0].fitness)
print(population[0].fitness)
plt.plot(myPlot)
plt.xlabel('Number of iterations')
plt.ylabel('Fitness of the population')
plt.show()
print("--- %s seconds ---" % (time() - start_time))