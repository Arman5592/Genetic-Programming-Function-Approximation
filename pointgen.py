from math import sin,cos,log, sqrt
import pandas as pd
import random

#generates y for x
def function(x, gerr=False):
    if gerr:
        return log(x) + sin(x**2) + 3 * cos(x) + random.gauss(0, 1)
    else:
        return log(x) + sin(x**2) + 3 * cos(x)

#generates our data
def generate_point_set(point_cnt, min_x, max_x):
    df = pd.DataFrame(columns=['x', 'y'])
    x = 0

    for i in range(0, point_cnt):
        x = random.randint(min_x, max_x)
        df.loc[i] = [x, function(x, False)]
    
    df.to_csv('points.csv', index=False)

# test functions
#generate_point_set()
