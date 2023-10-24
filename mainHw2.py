# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 16:34:16 2022

@author: Zolfaqar
"""
from numpy import arange
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi
from numpy import meshgrid
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from numpy import argsort
from numpy.random import randn
from numpy.random import rand
from numpy.random import seed
from numpy import asarray
from numpy import sin,sqrt
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
from chromosome import chromosome


def in_bounds(point, bounds):
	# enumerate all dimensions of the point
	for d in range(len(bounds)):
		# check if out of bounds for this dimension
		if point[d] < bounds[d, 0] or point[d] > bounds[d, 1]:
			return False
	return True


def schwefel( x ):  # schw.m
    x = np.asarray_chkfinite(x)
    n = len(x)
    return 418.9829*n - sum( x * sin( sqrt( abs( x ))))

        

def create_inital(population_size  , Dimention):
    population = []
    for i in range(population_size):
        a = chromosome()
        a.dimention = np.random.randint(-500,500,[Dimention])
        population.append(deepcopy(a))
    return population

def main(objective, bounds, n_iter, mu, lam, dim):
    best, best_eval = None, 1e+10
    tao = 1/((lam) ** (1/2))
    population = create_inital(lam , dim)
    how_many_children = int(lam / mu)
    
    for epoch in range(n_iter):
        print(epoch)
        scores = [c.evaluate() for c in population]
        
        ranks = argsort(argsort(scores))
        indexes = np.array(ranks).argsort()[:20]
        
        children = list()
        for i in indexes:
            if scores[i] < best_eval:
                best, best_eval = deepcopy(population[i] ) , deepcopy(scores[i])
                plt.scatter(epoch , best_eval)
                plt.pause(0.05)
                print(best_eval)
            counter = 0
            current_parrent = deepcopy(population[i])
            while(counter < how_many_children):
                sigma = current_parrent.sigma
                sigma = sigma * exp(tao*np.random.rand()) 
                child = chromosome()
                child.set_dimantation(current_parrent.dimention + randn(len(bounds)) * sigma)
                child.set_sigma(sigma)
                if(in_bounds(child.dimention, bounds)):
                    children.append(child)
                    counter+=1
        population = children
    plt.show()
    return [best, best_eval]
                
            
                
        
if __name__ == '__main__':
    inp = int(input("Enter the Number of dimention:"))
    bounds = asarray([[-500, 500]] * inp)
            
    best, score =  main(schwefel , bounds , 1000  , 1000 , 5000 , inp) 
    print('Done!')
    print('f(%s) = %f' % (best.dimention, score))
    