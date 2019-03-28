import pandas as pd
import random
import numpy as np
from scipy.spatial.distance import cdist

points = []
for i in range(100):
	points.append([random.uniform(0,255), random.uniform(0,255), random.uniform(0,255), random.uniform(0,255), random.uniform(0,255), random.uniform(0,255)])
points_frame = pd.DataFrame(points, columns=(list("XYZRGB")))

# def closest(df, x, y):
# 	closest_x = df.iloc[(df['X'] - x).abs().argsort()[:1]]
# 	closest_y = df.iloc[(df['Y'] - y).abs().argsort()[:1]]
# 	print(closest_x, closest_y)

# closest(points_frame, 40, 90)



print(closest(points_frame, 10, 20))