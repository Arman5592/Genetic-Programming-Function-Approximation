# Mohammad Arman Soleimani      98105835

from anytree import Node
import pandas as pd
from pointgen import generate_point_set
from arith import tree_mse,gen_baby_tree,print_tree
from nature import best_specimen, breed_population, mutate_population,natural_selection
import time

min_x = 0
max_x = 1000
point_cnt = 300
population_cnt = 500
rounds = 5

population = []
start_time = time.time()

# generate our function's points
generate_point_set(point_cnt, min_x, max_x)

df = pd.read_csv('points.csv')

# generate initial population
for _ in range(population_cnt*2):
    population.append(gen_baby_tree())

print(len(population))

natural_selection(population, population_cnt, df)
population = [i for i in population if i] #remove None values

# cycle of mutation, selection & breeding
for i in range(rounds):
    mutate_population(population, population_cnt)

    print(len(population))

    natural_selection(population, population_cnt, df)
    population = [i for i in population if i] #remove None values

    print(len(population))

    breed_population(population, population_cnt, df)
    population = [i for i in population if i] #remove None values

    print(len(population))

    print('round '+str(i))

result, result_mse = best_specimen(population, df)

end_time = time.time()

print('elapsed time:'+ str(end_time - start_time)) #elapsed time
print('best expression\'s mse:'+str(result_mse))
print('population:'+str(population_cnt))
print('generations:'+str(rounds))
print('blackbox points:'+str(point_cnt))

print_tree([result])
