from functools import cmp_to_key
from src.dataset import readData
from src.comparator import compare


class Chromosome:
    schedule = []  # list of numProcs lists having at most numTasks tasks
    numTasks = 0  # number of input tasks
    numProcs = 0  # number of input processors
    fitness = 0  # fitness of the chromosome
    initialized = False  # used to ensure readData() is called only once
    data = None  # data from the Kasahara dataset

    def __init__(self):
        if not Chromosome.initialized:
            Chromosome.initialized = True
            Chromosome.data = readData(0)
            Chromosome.numProcs = Chromosome.data['numProcs']
            Chromosome.numTasks = Chromosome.data['numTasks']
            del Chromosome.data['numProcs']
            del Chromosome.data['numTasks']
            Chromosome.data = list(Chromosome.data.values())
            # now, data is a list of task dictionaries sorted topologically
            # sort according to heights
            Chromosome.data.sort(key=cmp_to_key(compare))
            j = 0
            for i in Chromosome.data:  # save key for internal calculation later
                i['key'] = j
                j += 1
        self.schedule = [[] for i in range(0, Chromosome.numProcs)]

    # the fitness of a chromosome, currently, is its finishing time
    def calculateFitness(self):
        ftp = [0] * Chromosome.numProcs
        for i in range(0, Chromosome.numTasks):
            p = self.searchInProc(i)
            ftp[p] += Chromosome.data[i]['procTime']
            for j in range(0, Chromosome.numProcs):
                if p == j:
                    continue
                for k in self.schedule[j]:
                    temp = [k[i] for i in k if 'pre' in i]
                    if len(temp) > 0 and ftp[p] < ftp[j]:
                        ftp[p] = ftp[j] + Chromosome.data[i]['procTime']
                        break
        self.fitness = max(ftp)

    # to internally search for concerned processor of a task
    def searchInProc(self, task):
        for i in range(0, len(self.schedule)):
            for j in self.schedule[i]:
                if (task + 1) == j['procID']:
                    return i
