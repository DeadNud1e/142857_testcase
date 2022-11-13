import pandas as pd
import random
from random import randrange, sample
import datetime
import os



def generateData(ids, products, sartDate):
    output_path = 'task1/data.csv'
    if os.path.isfile(output_path) :
        return 'File already exists: ' + output_path
    
    with open(output_path, 'a') as file:
        for i in ids:
            n = random.randint(1,50)
            for j in sample(products,n):
                file.write(f"{i},{j},{startDate+ datetime.timedelta(minutes=randrange(60))}\n")
    return output_path



if __name__ == '__main__':
    ids = list(range(1,1001))
    products = list(range(1,51))
    startDate = datetime.datetime(2022, 11, 9,13, 00)
    generateData(ids, products, startDate)