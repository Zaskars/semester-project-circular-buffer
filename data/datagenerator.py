import csv
import random
import pandas as pd

def addgen():
    with open('data/add/dataset_step.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for i in range(10000):
            spamwriter.writerow([random.randrange(10000)])

def getgen():
    with open('data/get/dataset5_step.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for i in range(50000):
            spamwriter.writerow([random.randrange(10000)])

def setgen():
    with open('data/set/dataset5_step.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for i in range(50000):
            spamwriter.writerow([random.randrange(10000)])

def resizegen():
    with open('data/resize/dataset5_step.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for i in range(50000):
            spamwriter.writerow([random.randrange(10000)])




if __name__ == '__main__':
    addgen()
    #results = pd.read_csv('data/add/dataset5.csv')
    #print(len(results))
    #getgen()
    #setgen()
    #resizegen()
