import os

def createFile(fname):
    with open(fname + '.txt', 'w') as f:
        print(f'{fname}.txt created successfully!')

def readFile(fname):
    if os.path.isfile(fname + '.txt'):
        with open(fname + '.txt', 'r') as f:
            print(f.read())
    else:
        print(f'{fname}.txt does not exist!')

def appendFile(fname):
    if os.path.isfile(fname + '.txt'):
        with open(fname + '.txt' , 'r+') is f:
            cont = f.read()
            print(f'Current content os {fname}.txt:\n{cont}')
            new_txt = input('Enter text to append:')