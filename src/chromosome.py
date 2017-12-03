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

    def __init__(self, file=0):
        if not Chromosome.initialized:
            Chromosome.initialized = True
            Chromosome.data = readData(file)
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
        finishTime = [0] * Chromosome.numTasks
        for i in Chromosome.data:
            pre = []
            p = self.searchInProc(i)
            if self.schedule[p][0] != i:
                for j in range(0, len(self.schedule[p]) - 1):
                    if self.schedule[p][j + 1] == i:  # forced predecessor
                        pre.append(self.schedule[p][j]['procID'])
            for k in i:
                if 'pre' in k:
                    pre.append(i[k])
            if len(pre) > 0:
                finishTime[i['procID'] - 1] = max(
                    [finishTime[j - 1] for j in pre]) + i['procTime']
            else:
                finishTime[i['procID'] - 1] = i['procTime']
        self.fitness = max(finishTime)

    # to internally search for concerned processor of a task
    def searchInProc(self, task):
        x = 0
        for i in self.schedule:
            for j in i:
                if task == j:
                    return x
            x += 1
