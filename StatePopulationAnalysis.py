#!/usr/bin/env python3
import matplotlib.pyplot as plt
import matplotlib.animation as an
from matplotlib import style
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import pandas as pd
import csv

F_TSV = "C:/Users/mmuht/Desktop/INST326/Class Data/m2_statepopulation.tsv"
data_list = []
csv.register_dialect("escaped", delimiter='\t', escapechar=',')

def data(in_file):
    alist = []
    name = in_file
    with open("%s" % (name,), "r") as f:
        raw = csv.DictReader(f, dialect="escaped")
        for row in raw:
            data = {k.strip(' '): v.strip(' ') for k, v in row.items()}
            data_list.append(data)

def plot_insert_individual_dict(sample):
    plt.axis([1950,2010,0,60000000])
    plt.xlabel("Time in years")
    plt.ylabel("Population Size")
    y = []; p = [];
    x = sample.items()
    a = 0
    for year, population in x:
        name = sample['Name']
        if a == 0:
            plt.suptitle("%s" % name)
            a += 1
        if year != 'Name':
            year = int(year); population = int(population);
            y.append(year); p.append(population);
    plt.plot(y, p, 'ro')        
    plt.show()

def plot_all_states(sample):
    plt.axis([1950,2010,0,60000000])
    plt.xlabel("Time in years")
    plt.ylabel("Population Size")
    a_number = 0
    for i in sample:
        if a_number > 0:
            plt.figure()
            y = []; p = [];
            x = i.items()
            a = 0
            for year, population in x:
                name = i['Name']
                if a == 0:
                    plt.suptitle("%s" % name)
                    a += 1
                if year != 'Name':
                    year = int(year); population = int(population);
                    y.append(year); p.append(population);
            plt.plot(y, p, 'ro')        
            plt.show()
        a_number += 1
               
def main():
    data(F_TSV)
    plot_all_states(data_list) ##while this will loop through all the states
    #plot_insert_individual_dict(data_list[2]) ## This will output a single state in
    #a plot
    ## the first option you have to cancel out of each plot to see the next
    # states data

if __name__ == '__main__':
    main()

