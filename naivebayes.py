def read_file(filename):
    data=[]
    with open('filename') as file:
        next(file)
        for line in file:
            row=line.strip.split(',')
            features=row[1:-1]
            label=row[-1]
            data.append((features,label))
    return data
