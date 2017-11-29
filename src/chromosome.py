from functools import cmp_to_key

from src.dataset import readData
from src.comparator import compare


class Chromosome:  # done
    schedule = []        # list of numProcs lists having at most numTasks tasks
    numTasks = 0         # number of input tasks
    numProcs = 0         # number of input processors
    fitness = 0          # fitness of the chromosome
    initialized = False  # used to ensure readData() is called only once
    data = None          # data from the Kasahara dataset

    def __init__(self):
        pass

    # the fitness of a chromosome, currently, is its finishing time
    def calculateFitness(self):
        if not Chromosome.initialized:
            Chromosome.initialized = True
            Chromosome.data = readData(0)
            Chromosome.numProcs = Chromosome.data['numProcs']
            Chromosome.numTasks = Chromosome.data['numTasks']
            del Chromosome.data['numProcs']
            del Chromosome.data['numTasks']
            Chromosome.data = list(Chromosome.data.values())
            # sort according to heights
            Chromosome.data.sort(key=cmp_to_key(compare))
            j = 0
            for i in Chromosome.data:  # save key for internal calculation later
                i['key'] = j
                j += 1
        # for i in Chromosome.data:
            # calculation of fitness is incomplete
