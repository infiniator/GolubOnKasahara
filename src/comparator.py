def compare(x, y):
    if x['height'] < y['height']:
        return -1
    elif x['height'] > y['height']:
        return 1
    elif x['procID'] < y['procID']:
        return -1
    else:
        return 1


def compareChromosomes(x, y):
    if x.fitness > y.fitness:
        return 1
    elif x.fitness < y.fitness:
        return -1
    else:
        return 0
