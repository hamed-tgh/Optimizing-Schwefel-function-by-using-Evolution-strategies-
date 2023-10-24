# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 18:54:58 2022

@author: Hamed
"""

from numpy import sin,sqrt
import numpy as np


def schwefel( x ):  # schw.m
    x = np.asarray_chkfinite(x)
    n = len(x)
    return 418.9829*n - sum( x * sin( sqrt( abs( x ))))

class chromosome():
    def __init__(self):
        self.dimention = []
        self.sigma = np.random.rand()
        self.score = 0
    def evaluate(self):
        self.score = schwefel(self.dimention)
        return self.score
        
    def set_dimantation(self , new_dmaentation):
        self.dimention = new_dmaentation
    def set_sigma(self,sigma):
        self.sigma = sigma

