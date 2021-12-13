from anytree import Node,RenderTree
from math import sin,cos,log,ceil
import pandas as pd
import random

# takes an expression tree, calculates y for x
def tree_point(node, x):
    if node.is_leaf:
        if node.name == 'x':
            return x
        else:
            return float(node.name)
    else:
        if node.name == 'exp':
            try:
                return float(tree_point(node.children[0], x)) ** ceil(float(tree_point(node.children[1], x)))
            except:
                if float(tree_point(node.children[1], x)) > 0:
                    return abs(float(tree_point(node.children[0], x)))
                else:
                    return float(tree_point(node.children[0], x))
        elif node.name == 'div':
            try:
                return float(tree_point(node.children[0], x)) / float(tree_point(node.children[1], x))
            except:
                return float(tree_point(node.children[0], x))
        elif node.name == 'mul':
            try:
                return float(tree_point(node.children[0], x)) * float(tree_point(node.children[1], x))
            except:
                if float(tree_point(node.children[1], x)) > 0:
                    return float(tree_point(node.children[0], x))
                else:
                    return float(tree_point(node.children[0], x)) * - 1
        elif node.name == 'sum':
            try:
                return float(tree_point(node.children[0], x)) + float(tree_point(node.children[1], x))
            except:
                return float(tree_point(node.children[0], x)) / 3 + float(tree_point(node.children[1], x)) / 3
        elif node.name == 'sub':
            try:
                return float(tree_point(node.children[0], x)) - float(tree_point(node.children[1], x))
            except:
                return float(tree_point(node.children[0], x)) / 3 - float(tree_point(node.children[1], x)) / 3
        elif node.name == 'sin':
            try:
                return sin(float(tree_point(node.children[0], x)))
            except:
                return 0.5
        elif node.name == 'cos':
            try:
                return cos(float(tree_point(node.children[0], x)))
            except:
                return 0.5
        elif node.name == 'log':
            try:
                return log(abs(float(tree_point(node.children[0], x))))
            except:
                return 1.00
        else:
            return 1.00

# returns mse for an expression tree
def tree_mse(node, df):
    err = float(0)

    for index, row in df.iterrows():
        x, y = row['x'], row['y']

        diff = float(tree_point(node, x) - y)
        err = err + (diff/df.shape[0]) * diff
    
    return err

# generates random baby tree
def gen_baby_tree():
    r = random.randint(0, 7)

    if r > 4 and random.randint(0, 1)==0:
        r = r - 3

    root = Node('operator')
    child1 = Node('operand1')
    child2 = Node('operand2')

    if r==0:
        root = Node('exp')
    elif r==1:
        root = Node('div')
    elif r==2:
        root = Node('mul')
    elif r==3:
        root = Node('sum')
    elif r==4:
        root = Node('sub')
    elif r==5:
        root = Node('sin')
    elif r==6:
        root = Node('cos')
    else:
        root = Node('log')
    
    rc1 = random.randint(0, 1)
    rc2 = random.randint(0, 1)

    if rc1==0:
        child1 = Node('x', parent=root)
    else:
        rg = random.gauss(0, 1) * 10.00
        if r==7:
            rg = abs(rg)
        child1 = Node(str(rg), parent=root)

    if r < 5:
        if rc2==0:
            child2 = Node('x', parent=root)
        else:
            rg = random.gauss(0, 1) * 10.00
            if r==7:
                rg = abs(rg)
            child2 = Node(str(rg), parent=root)

    return root

# saves a list of trees in txt files
def print_tree(trees):
    i = 0
    for tree in trees:
        tree_str = ''

        for pre, fill, node in RenderTree(tree):
            tree_str += "%s%s" % (pre, node.name) + '\n'
    
        f = open("tree"+str(i)+".txt", "w", encoding='utf-8')
        f.write(tree_str.strip())
        f.close()
        i = i + 1

    return tree_str.strip()


# test functions
#root = Node('sum')
#l1 = Node('exp', parent=root)
#l11 = Node('x', parent=l1)
#l12 = Node('2', parent=l1)
#r1 = Node('2.2', parent=root)
#r11 = Node('100', parent=r1)
#df = pd.read_csv('points.csv')
#print(tree_mse(root, df))
