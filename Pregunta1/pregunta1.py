# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 20:12:30 2020

@author: EnriqueCondori
"""
import array
import random
import pandas as pd
import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

heart =pd.read_csv('data.csv')
x=numpy.array(heart['CP'])
y=numpy.array(heart['trestbps asintomáticos'])
z=numpy.array(heart['fbs'])
#print(x)
# ------------CP
# tipo de dolor en el pecho
# - Valor 1: angina típica
# - Valor 2: angina atípica
# - Valor 3: dolor no anginal
#------------trestbps asintomáticos
# presión arterial en reposo (en mm Hg al ingreso al hospital)
#------------fbs
# presión arterial en reposo (en mm Hg al ingreso al hospital)

IND_SIZE =10
creator.create("FitnessMin", base.Fitness, weights=(1.0,))
creator.create("Individual", array.array, typecode='i', fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("indices", random.sample, range(IND_SIZE), IND_SIZE)

toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)

# toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.indices, 100)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalTSP(individual):
    distance =0
    distance += x[individual[0]]+y[individual[1]]+z[individual[2]]
    return distance,


toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.07)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evalTSP)

def main():
    random.seed(64)

    pop = toolbox.population(n=10)

    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    
    algorithms.eaSimple(pop, toolbox, 0.7, 0.2, 100, stats=stats,halloffame=hof)
    
    return pop, stats, hof

if __name__ == "__main__":
    pop,stats,hof=main()
    # print(pop)
    # print(stats)