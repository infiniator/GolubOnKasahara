def readData(id):
    if id < 10:
        id = '000' + str(id)
    else:
        if id < 100:
            id = '00' + str(id)
        else:
            id = '0' + str(id)
    id = 'rand' + id
    file = open(id, 'r')
    data = 0  # calculate
    return data