import csv

def load_diamonds_from_csv(filename):
    diamonds = []
    try:
        with open(filename, 'r') as file:
            headers = file.readline().strip().split(',')
            for line in file:
                values = line.strip().split(',')
                diamond = {headers[i]: values[i] for i in range(len(headers))}
                diamond['carat'] = float(diamond['carat'])
                diamond['depth'] = float(diamond['depth'])
                diamond['table'] = float(diamond['table'])
                diamond['price'] = int(diamond['price'])
                diamond['x'] = float(diamond['x'])
                diamond['y'] = float(diamond['y'])
                diamond['z'] = float(diamond['z'])
                diamonds.append(diamond)
    except FileNotFoundError:
        print('File not found')
    return diamonds