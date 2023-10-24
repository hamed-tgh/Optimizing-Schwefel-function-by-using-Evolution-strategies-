# Optimizing-Schwefel-function-by-using-Evolution-strategies-


#Introduction

In computer science, an evolution strategy (ES) is an optimization technique based on ideas of evolution. It belongs to the general class of  evolutionary computation or artificial evolution methodologies.

#history

The 'evolution strategy' optimization technique was created in the early 1960s and developed further in the 1970s and later by Ingo Rechenberg, Hans-Paul schwefel and their co-workers. 


Evolution strategies is a stochastic global optimization algorithm.
It is an evolutionary algorithm related to others, such as the genetic algorithm, although it is designed specifically for continuous function optimization.
So we should Note that:
1.	Evolution Strategies is a stochastic global optimization algorithm inspired by the biological theory of evolution by natural selection.
2.	There is a standard terminology for Evolution Strategies and two common versions of the algorithm referred to as (mu, lambda)-ES and (mu + lambda)-ES.
3.	How to implement and apply the Evolution Strategies algorithm to continuous objective functions.

# Implementation Details
I developed (mu,lamda)-ES in this homework in order to find minimum of value of Schwefel benchmark in range of (500,500).

HINT:
	Any chromosome or any created child must check to locate in valid range.
	In this homework I used sigma-first mutation
 
sigma= sigma*exp⁡( Tao*Normal )
X=X+Normal*sigma 
With Pm = 1


	Parent selection I involve fitness to make higher pressure 
	Generational model is used for survival selection 

REMEMBER:
In ES, cross over have no effect on optimization. So I set pc = 0 


the bellow image illustates Best Fitness function value during Optimization for d=2

![image](https://github.com/hamed-tgh/Optimizing-Schwefel-function-by-using-Evolution-strategies-/assets/47190471/58c21ac6-29f7-44a6-8f60-735af60913de)

