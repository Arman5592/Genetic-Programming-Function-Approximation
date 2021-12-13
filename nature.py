from anytree import Node
import pandas as pd
from pointgen import generate_point_set
from arith import tree_mse,gen_baby_tree,print_tree
import random
from copy import deepcopy

# replaces 1 or 2 leaf/leaves with a baby tree
def mutate_tree(tree):
    r = random.randint(1, 2)
    
    for _ in range(0, r):
        node = tree
        c = 0
        while not(node.is_leaf):
            c = random.randint(0, len(node.children)-1)
            node = node.children[c]
        
        parent = node.parent
        if c==1:
            parent.children = [parent.children[0], gen_baby_tree()]
        elif len(parent.children) != 1:
            parent.children = [gen_baby_tree(), parent.children[1]]
        else:
            parent.children = [gen_baby_tree()]
        #node = gen_baby_tree()
    
    return tree


# adds a mutated copy of each tree to the population ()
def mutate_population(population, population_cnt): 
    for i in range(population_cnt):
        population.append(mutate_tree(population[i]))

# generates sets of two indices
def gen_pairs(population_cnt):
    indices = list(range(0, population_cnt*2))
    pairs = []
    i1, i2 = 0, 0
    r1, r2 = 0, 0

    for _ in range(0, population_cnt):
         r1 = random.randint(0, len(indices)-1)
         i1 = indices[r1]
         del indices[r1]
         r2 = random.randint(0, len(indices)-1)
         i2 = indices[r2]
         del indices[r2]
         pairs.append((i1, i2))
    
    return pairs

# cuts population in half
def natural_selection(population, population_cnt, df):
    
    pairs = gen_pairs(population_cnt)

    # from each pair of indices, choose the better tree
    for i in range(0, population_cnt):
        i1, i2 = pairs[i][0], pairs[i][1]
        mse1 = tree_mse(population[i1], df)
        mse2 = tree_mse(population[i2], df)

        if mse2 < mse1:
            i1, i2 = i2, i1
        
        population[i2] = None
            
# breeds two trees, generates a third tree (child)
def breed_trees(tree1, tree2):

    root = deepcopy(tree1)
    if len(tree1.children)>1:
        r1 = random.randint(0, len(tree1.children)-1)
    else:
        r1 = 0
    if len(tree2.children)>1:
        r2 = random.randint(0, len(tree2.children)-1)
    else:
        r2 = 0

    if r1==1:
        root.children = [deepcopy(root.children[0]), deepcopy(tree2.children[r2])]
    elif len(root.children) != 1:
        root.children = [deepcopy(tree2.children[r2]), deepcopy(root.children[1])]
    else:
        root.children = [deepcopy(tree2.children[r2])]
    
    return root

# performs breeding on the entire population
def breed_population(population, population_cnt, df):
    pairs = gen_pairs(int(population_cnt/2))

    for pair in pairs:
        child = breed_trees(population[pair[0]], population[pair[1]])

        if tree_mse(population[pair[0]], df) > tree_mse(child, df):
            if tree_mse(population[pair[0]], df) > tree_mse(population[pair[1]], df):
                #parent[0] has the highest error
                population[pair[0]] = None
                population.append(child)
        elif tree_mse(population[pair[1]], df) > tree_mse(child, df):
            if tree_mse(population[pair[1]], df) > tree_mse(population[pair[0]], df):
                #parent[1] has the highest error
                population[pair[1]] = None
                population.append(child)

# returns the best tree
def best_specimen(population, df):
    best = Node('player 456')
    best_mse = tree_mse(population[0], df)
    mse = 0

    for specimen in population:
        mse = tree_mse(specimen, df)
        if mse < best_mse:
            best_mse = mse
            best = specimen
    
    return best, best_mse

    

#root = Node('sum')
#l1 = Node('exp', parent=root)
#l11 = Node('x', parent=l1)
#l12 = Node('2', parent=l1)
#r1 = Node('2.2', parent=root)

#root2 = Node('mul')
#l1 = Node('sub', parent=root2)
#l11 = Node('5', parent=l1)
#l12 = Node('15', parent=l1)
#r1 = Node('x', parent=root2)

#print_tree([root,root2,breed_trees(root, root2)])
