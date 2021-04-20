# Genetic algorithem

## Prerequisites:
* Conda 4.9.2
* JetBrains IDE
## Installation
* Open a terminal in the folder named "genetic-algo-dussan"
* Then write: "jupyter notebook"
* If you have problems openning a jupyeter notebook: <a href="https://jupyter.readthedocs.io/en/latest/running.html"> How to  open a notebook</a>
## You can directly see the experiment implementation 
* Experiment implementation: <a href="https://github.com/joangerard/genetic-algo-dussan/blob/main/Experiments.ipynb"> Implementation 😊 </a>
## Introduction:
In the following work 3 different basic problems are solved using the genetic algorithm. In addition, a series of experiments are made by making small changes in the variables of the algorithm in order to better understand the algorithm and have better results.
## 1. First Problem
In this first problem, we have an initial population of 100 random chromosomes, each with 20 genes, which can have only two values, 0 and 1, which must be random for each chromosome.

As "Fitness function" the amount of "1" in the genes was counted, which means that the strongest FF is 20.

### First Experiment
#### Experiment parameters:
* Crossover probability: 0.7
* Mutation probability: 0.001
* Population size: 100 [chromosomes]
* Number of tests: 20
#### Best result:
* Experiment: 0
* Number of generations: 15
* Max FF: 20
* Min FF: 11
* Mean FF: 14.66 

<div style="text-align:center"><img src="https://github.com/joangerard/genetic-algo-dussan/blob/main/imagenes/1_exp_br_png.png" />
  
#### Worst result:
* Experiment: 17
* Number of generations: 431
* Max FF: 20
* Min FF: 18
* Mean FF: 18.98 

<div style="text-align:center"><img src="https://github.com/joangerard/genetic-algo-dussan/blob/main/imagenes/1_exp_wr_png.png" />
 
#### Average Result
* The average of generations required to find the strongest FF is 47.6
#### Conclution:
* The number of iterations it takes to obtain a result varies between experiments, due to the initial population and also to the random values of mutations and crossovers

### Second experiment:
#### Experiment parameters:
* Crossover probability: 0
* Mutation probability: 0.001
* Population size: 100 [chromosomes]
* Number of tests: 20
#### Average result
The average of generations required to find the strongest FF is 1000.0
#### Conclution
* Because mutation is very unlikely, generations would not change much from generation to generation. Which would prevent the strongest FF from being found. It would take many generations to achieve that goal and good luck

### Third Experiment
#### Experiment parameters:
* Crossover probability: 0.7
* Mutation Chance: 0
* Population size: 100 [chromosomes]
* Number of tests: 20
#### Best result:
* Experiment: 18
* Number of generations: 20
* Max FF: 20
* Min FF: 12
* Mean FF: 15.726 

<div style="text-align:center"><img src="https://github.com/joangerard/genetic-algo-dussan/blob/main/imagenes/3_exp_br_png.png" />
  
#### Worst result:
* Experiment: 17
* Number of generations: 1000
* Max FF: 19
* Min FF: 19
* Mean FF: 19 

<div style="text-align:center"><img src="https://github.com/joangerard/genetic-algo-dussan/blob/main/imagenes/3_exp_wr_png.png" />
  
#### Average Result
* The average of generations required to find the strongest FF is 81.5
#### Conclution:
* At first glance one might think that a good idea would be to dispense with the mutation, however, in the experiment it was observed that the worst case scenario remained constant for more than 800 generations with an exactly the same population of chromosomes with an FF of 19. Precisely for this case the mutation would have been very useful

### Fourth experiment
#### Experiment parameters:
* Crossover probability: 0.9
* Mutation probability: 0.001
* Population size: 100 [chromosomes]
* Number of tests: 20
#### Best result:
* Experiment: 17
* Number of generations: 7
* Max FF: 20
* Min FF: 8
* Mean FF: 13.79 

<div style="text-align:center"><img src="https://github.com/joangerard/genetic-algo-dussan/blob/main/imagenes/4_exp_rr_png.png" />
  
#### Worst result:
* Experiment: 6
* Number of generations: 44
* Max FF: 20
* Min FF: 14
* Mean FF: 17.37 

<div style="text-align:center"><img src="https://github.com/joangerard/genetic-algo-dussan/blob/main/imagenes/4_exp_wr_png.png" />
  
#### Average Result
* The average of generations required to find the strongest FF is 21.75
#### Conclution:
* For this particular experiment it seems that having a high crossover is a great advantage. 

### Fifth Experiment
#### Experiment parameters:
* Crossover probability: 0.3
* Mutation probability: 0.001
* Population size: 100 [chromosomes]
* Number of tests: 20
#### Best result:
* Experiment: 18
* Number of generations: 18
* Max FF: 20
* Min FF: 10
* Mean FF: 16.48 

<div style="text-align:center"><img src="https://github.com/joangerard/genetic-algo-dussan/blob/main/imagenes/5_exp_br_png.png" />
  
#### Worst result:
* Experiment: 5
* Number of generations: 1000
* Max FF: 19
* Min FF: 18
* Mean FF: 18.96 

<div style="text-align:center"><img src="https://github.com/joangerard/genetic-algo-dussan/blob/main/imagenes/5_exp_wr_png.png" />
  
#### Average Result
* The average of generations required to find the strongest FF is 232.35
#### Conclution:
* A low crossover does not allow most experiments to find the strongest chromosome, although the generations get stronger and stronger. This may be due to the selection of chromosomes based on probabilistic weights on their FF. Making a comparison with the previous examples, it can be seen that the average of the generations of the experiments is much better with a crossover probability of 0.9 and with a mutation probability of 0.001. This is reflected in the calculated average of the fourth experiment, 21.75, which is much lower than our previous experiments.

### Sixth Experiment
#### Experiment parameters:
* Crossover probability: 0.7
* Mutation probability: 0.001
* Population size: 50 [chromosomes]
* Number of tests: 20
#### Best result:
* Experiment: 15
* Number of generations: 12
* Max FF: 20
* Min FF: 10
* Mean FF: 14.44 

<div style="text-align:center"><img src="https://github.com/joangerard/genetic-algo-dussan/blob/main/imagenes/6_exp_br_png.png" />
  
#### Worst result:
* Experiment: 3
* Number of generations: 312
* Max FF: 20
* Min FF: 19
* Mean FF: 19.02 

<div style="text-align:center"><img src="https://github.com/joangerard/genetic-algo-dussan/blob/main/imagenes/6_exp_wr_png.png" />
  
#### Average Result
* The average of generations required to find the strongest FF is 44.05
#### Conclution:
* Better results were obtained than in the first experiment



### Seventh Experiment
#### Experiment parameters:
* Crossover probability: 0.7
* Mutation probability: 0.001
* Population size: 500 [chromosomes]
* Number of tests: 20
#### Best result:
* Experiment: 7
* Number of generations: 16
* Max FF: 20
* Min FF: 13
* Mean FF: 16.46 

<div style="text-align:center"><img src="https://github.com/joangerard/genetic-algo-dussan/blob/main/imagenes/7_exp_br_png.png" />

#### Worst result:
* Experiment: 2
* Number of generations: 56
* Max FF: 20
* Min FF: 16
* Mean FF: 17.99 

<div style="text-align:center"><img src="https://github.com/joangerard/genetic-algo-dussan/blob/main/imagenes/7_exp_wr_png.png" />
  
#### Average Result
* The average of generations required to find the strongest FF is 27.4
#### Conclution:
* This experiment was by far the best so far, it can be said that having a high population prevents chromosomes from having exactly the same value before finding the strongest chromosome


### Eighth Experiment
#### Experiment parameters:
* Crossover probability: 0.7
* Mutation probability: 0.001
* Population size: 1000 [chromosomes]
* Number of tests: 20
#### Best result:
* Experiment: 5
* Number of generations: 5
* Max FF: 20
* Min FF: 4
* Mean FF: 11.971 

<div style="text-align:center"><img src="https://github.com/joangerard/genetic-algo-dussan/blob/main/imagenes/8_exp_br_png.png" />
 
#### Worst result:
* Experiment: 18
* Number of generations: 18
* Max FF: 20
* Min FF: 10
* Mean FF: 15.537 

<div style="text-align:center"><img src="https://github.com/joangerard/genetic-algo-dussan/blob/main/imagenes/8_exp_wr_png.png" />
  
#### Average Result
* The average of generations required to find the strongest FF is 12.0
#### Conclution:
* This experiment is the one that had the best result, of all the experiments within this experiment they had superior results than the previous ones, which indicates that having a high population is crucial to having good results. A large population can be an important factor, because it prevents genes from being identical in just a few generations. In addition, it allows that there is more probability that all genes have a value of 1 in some chromosome of the population, which is very beneficial for the algorithm.


## 2. Second Problem
In this second problem we have an initial population of 100 random chromosomes, each with 20 genes, which can have only 10 values, 0-9, which must be random for each chromosome.

The objective was to find a chromosome whose genes were all of value "1", the FF that was used was the following:
for gene in genes: 

<div style="text-align:center"><img src="https://github.com/joangerard/genetic-algo-dussan/blob/main/imagenes/allones.png" />
  
In this way the strongest chromosome would have a value of 38.400

### Tenth Experimet
#### Experiment parameters:
* Crossover probability: 0.7
* Mutation probability: 0.001
* Population size: 100 [chromosomes]
* Number of tests: 10
* FF: All ones
#### Average Result
* The average of generations required to find the strongest FF is 1000.0
#### Conclution:
* The strongest chromosome was not found, it is suspected that this is because the population of chromosomes is not large and diverse enough for the range of values that each gene can take.


### Eleventh Experimet
#### Experiment parameters:
* Crossover probability: 0.8
* Mutation probability: 0.005
* Population size: 500 [chromosomes]
* Number of tests: 10
* FF: All ones
#### Best result:
Experiment: 7
* Number of generations: 39
* Max FF: 38400
* Min FF: 18900
* Mean FF: 28418.82 

<div style="text-align:center"><img src="https://github.com/joangerard/genetic-algo-dussan/blob/main/imagenes/11_exp_br_png.png" />
  
#### Worst result:
* Experiment: 5
* Number of generations: 68
* Max FF: 38400
* Min FF: 26220
* Mean FF: 32652.48 

<div style="text-align:center"><img src="https://github.com/joangerard/genetic-algo-dussan/blob/main/imagenes/11_exp_wr_png.png" />
  
#### Average Result
* The average of generations required to find the strongest FF is 53.0
#### Conclution:
* Compared to the previous experiment, it was observed that increasing the chromosome population is very important to improve the performance of the algorithm in this experiment

## 3. Third Problem (Problem of the 8 queens)

The genes on the chromosomes were first designed to represent the checkerboard situation. It was decided that the genes per chromosome were 8, where each gene represents a column of the board, in its respective position. The content of each gene would be equal to the row occupied by the queen.

The FF used was "queens in peace" which basically means that the FF is equal to the number of queens that do not attack each other.

### Twelfth Experimet
#### experiment parameters:
* Crossover probability: 0.8
* Mutation probability: 0.005
* Population size: 500 [chromosomes]
* Number of tests: 10
* FF: queens in peace
#### Best result:
* Experiment: 8
* Number of generations: 44
* Max FF: 28
* Min FF: 15
* Mean FF: 21.946 

<div style="text-align:center"><img src="https://github.com/joangerard/genetic-algo-dussan/blob/main/imagenes/12_exp_br_png.png" />
  
* Solutions found: [3, 1, 7, 4, 6, 0, 2, 5]

<div style="text-align:center"><img src="https://github.com/joangerard/genetic-algo-dussan/blob/main/imagenes/solution.png" />
  
Don't judge my paint abilities  😂
#### Worst result:
* Experiment: 7
* Number of generations: 1000
* Max FF: 26
* Min FF: 23
* Mean FF: 25.944 

<div style="text-align:center"><img src="https://github.com/joangerard/genetic-algo-dussan/blob/main/imagenes/12_exp_wr_png.png" />
  
#### Average Result
* The average of generations required to find the strongest FF is 178.3
#### Conclution:
* The solution to this problem could be found through a high population of chromosomes
