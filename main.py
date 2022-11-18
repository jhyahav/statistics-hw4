from math import ceil

import pandas as pd
import matplotlib.pyplot as pl
import numpy as np
import scipy.stats as stats

# q1
path = "./heights.csv"
df = pd.read_csv(path)
df = df.sort_values("HEIGHT")
heights = df["HEIGHT"].to_numpy()
weights = df["WEIGHT"].to_numpy()
# section  a
pl.scatter(x=heights, y=weights, color="black", marker=".")

# sections b, d, e
MAX_X = 1500
median = lambda data: data[ceil(data.size / 2) - 1 * (data.size + 1 % 2)]
[lower, mid, upper] = np.array_split(df, 3)
lower_heights = lower["HEIGHT"].to_numpy()
lower_weights = lower["WEIGHT"].to_numpy()
lower_weights.sort()
upper_heights = upper["HEIGHT"].to_numpy()
upper_weights = upper["WEIGHT"].to_numpy()
upper_weights.sort()
x_lower = median(lower_heights)
y_lower = median(lower_weights)
x_upper = median(upper_heights)
y_upper = median(upper_weights)

b_RL = (y_upper - y_lower) / (x_upper - x_lower)
print(b_RL)

r_is = []
for i in range(heights.size):
    r_i = weights[i] - b_RL * heights[i]
    r_is.append(r_i)
r_is.sort()
a_RL = median(np.array(r_is))
print(a_RL)

x_RL = np.linspace(50, MAX_X, 1000)
y_RL = a_RL + b_RL * x_RL

pl.plot(x_RL, y_RL, "red")
pl.scatter([x_lower, x_upper],  [y_lower, y_upper], color="red")

var_x = np.var(heights)
cov_x_y = np.cov(heights, weights)[0][1]
x_avg = heights.sum() / heights.size
y_avg = weights.sum() / weights.size

b_LS = cov_x_y / var_x
a_LS = y_avg - b_LS * x_avg

x_LS = np.linspace(50, MAX_X, 1000)
y_LS = a_LS + b_LS * x_LS
pl.plot(x_LS, y_LS, "blue")

pl.title("Correlation btw Height & Weight, w/ Resistant Line and RSS - Full Dataset")
pl.xlabel("Height")
pl.ylabel("Weight")
pl.show()