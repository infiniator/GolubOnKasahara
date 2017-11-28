from src.dataset import readData


class Chromosome:  # done
    schedule = []        # list of numProcs lists having at most numTasks tasks
    numTasks = 0         # number of input tasks
    numProcs = 0         # number of input processors
    fitness = 0          # fitness of the chromosome
    initialized = False  # used to ensure readData() is called only once
    data = None          # data from the Braun dataset

    def __init__(self, tasks=512, procs=16):
        self.numTasks = tasks
        self.numProcs = procs
        for i in range(0, self.numProcs):
            self.schedule.append([0] * self.numTasks)

    # the fitness of a chromosome, currently, is its finishing time
    def calculateFitness(self):
        if not Chromosome.initialized:
            Chromosome.data = readData()
            Chromosome.initialized = True
        ftp = [0] * self.numProcs
        for i in range(0, self.numProcs):
            for j in range(0, len(self.schedule[i])):
                ftp[i] += Chromosome.data[self.schedule[i][j]][i]
        for i in range(0, len(ftp)):
            self.fitness += ftp[i]
