from functools import cmp_to_key
from random import randrange
from src.chromosome import Chromosome
from bisect import bisect_left
from src.binary_search import binarySearch
from src.comparator import compare


def initialisation():  # done
    population = []  # a list of chromosomes
    tempChromosome = Chromosome()
    # a temporary chromosome to be manipulated before adding to the population
    for i in range(0, 100):
        for j in Chromosome.data:
            k = randrange(0, Chromosome.numProcs)
            tempChromosome.schedule[k].append(j)
        for j in range(0, Chromosome.numProcs):
            tempChromosome.schedule[j].sort(key=cmp_to_key(compare))
        tempChromosome.calculateFitness()
        population.append(tempChromosome)
        tempChromosome = Chromosome()
    return population


def selection():
    print("he")


def crossover(a, b):
    randProc = randrange(0, Chromosome.numProcs)
    randTask = randrange(0, Chromosome.numTasks)
    indexA = -1
    indexB = -1
    for i in range(0, Chromosome.numProcs):
        indexB = binarySearch(b[i], randTask)
        indexA = binarySearch(a[i], randTask)


def mutation(a):  # done
    removeFrom = -1
    addTo = -1
    while removeFrom == addTo and len(a.schedule[removeFrom]) > 0:
        removeFrom = randrange(0, Chromosome.numProcs)
        addTo = randrange(0, Chromosome.numProcs)
    randTask = randrange(0, len(a.schedule[removeFrom]))
    a.schedule[addTo].insert(
        bisect_left(
            [i['key'] for i in a.schedule[addTo]],
            a.schedule[removeFrom][randTask]['key']
        ),
        a.schedule[removeFrom][randTask]
    )
    del a.schedule[removeFrom][randTask]
    return a
