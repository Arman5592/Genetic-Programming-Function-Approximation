# Genetic-Programming-Function-Approximation

### Introduction
This is a minimalist genetic program which approximates a function (expression tree) from points (x, y).
The main goal has been simplicity, which has hindered the program's performance but makes the code easier
to follow.

### Prerequisites
anytree
pandas
default libraries: time, math, random, copy

### Application
Can approximate a function f(x) from points in a csv file. 'pointgen.py' can be utilized to generate such points.
The result is saved in tree0.txt, as an expression tree.

### How to use
The GP performs approximation on a two-column (x and y) csv file named 'points.csv' within the same directory. 
In its current form, the program generates such a file using the functions in 'pointgen.py'.
The source function - used to generate the points for approximation - can be changed within 
'function' in 'pointgen.py'. Currently, it is set to ln(x) + sin(x^2) + 3cos(x), without any noise.
Noise can be enabled by calling function(x, True) in line 19 of 'pointgen.py'.

### GP Hyperparameters
Some parameters can be changed in 'project.py':

##### min_x, max_x
These determine the minimum and maximum x for our function points - big/small values can cause overflow,
but a smaller range for x can result in an overfit function.

##### point_cnt
The number of points used for approximation. More points usually result in a better approximation, but
slow down the program.

##### population_cnt
Our GP's population - this determines how many expression trees we keep in each generation. A higher
number for this parameters increases the chances of finding a better function, at the cost of execution speed.

##### rounds
Rounds in which the GP cycle is executed. More rounds results in more sophisticated result, but increases
overfitting and deepens the expression tree, which might result in a worse result.
