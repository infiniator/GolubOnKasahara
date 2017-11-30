from functools import cmp_to_key
from random import randrange
from src.chromosome import Chromosome
from bisect import bisect_left
from src.comparator import compare
from copy import copy


def initialisation(populationSize):  # done
    population = []  # a list of chromosomes
    tempChromosome = Chromosome()
    # a temporary chromosome to be manipulated before adding to the population
    for i in range(0, populationSize):
        for j in Chromosome.data:
            k = randrange(0, Chromosome.numProcs)
            tempChromosome.schedule[k].append(j)
        for j in range(0, Chromosome.numProcs):
            tempChromosome.schedule[j].sort(key=cmp_to_key(compare))
        tempChromosome.calculateFitness()
        population.append(tempChromosome)
        tempChromosome = Chromosome()
    return population


def selection(population, k):  # tournament selection is used
    best = None
    for i in range(0, k):
        index = population[randrange(0, len(population))]
        if best is None or best.fitness > index.fitness:
            best = index
    return best


def crossover(a, b):
    candidate1 = [0] * Chromosome.numTasks
    candidate2 = [0] * Chromosome.numTasks
    for i in range(0, len(a.schedule)):
        for j in range(0, len(a.schedule[i])):
            candidate1[Chromosome.data[j - 1]['key']] = i
    for i in range(0, len(b.schedule)):
        for j in range(0, len(b.schedule[i])):
            candidate2[Chromosome.data[j - 1]['key']] = i
    r = randrange(1, Chromosome.numTasks - 1)
    new1 = candidate1[:r] + candidate2[r:]
    new2 = candidate2[:r] + candidate1[r:]
    tempChromosome = Chromosome()
    temp2 = Chromosome()
    for i in range(0, len(new1)):
        tempChromosome.schedule[new1[i]].append(Chromosome.data[i])
        temp2.schedule[new2[i]].append(Chromosome.data[i])
    return tempChromosome, temp2


def mutation(a):  # done
    removeFrom = -1
    addTo = -1
    a = copy(a)
    if len([len(i) for i in a.schedule if len(i) > 0]) > 1:
        while removeFrom == addTo and len(a.schedule[removeFrom]) == 0:
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
