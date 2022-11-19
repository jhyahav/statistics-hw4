import scipy.stats as sc
import numpy as np
import matplotlib.pyplot as pl

# q2
# section a
x = sc.norm.rvs(loc=5, scale=1, size=30)

# section b
y = 5*x + 2

# section c
corr = np.corrcoef(x, y)[0][1]
print("Empirical correlation coefficient:", corr)

# section d
b_LS = np.cov(x, y)[0][1] / np.var(x)
print("Empirical sum of least squares slope:", b_LS)

# section e
noise = sc.norm.rvs(loc=0, scale=1, size=30)
y = y + noise
noisy_corr = np.corrcoef(x, y)[0][1]
print("Empirical correlation coefficient with noise:", noisy_corr)
noisy_b_LS = np.cov(x, y)[0][1] / np.var(x)
print("Empirical sum of least squares slope with noise:", noisy_b_LS)

# sections f,g
base_y = 5*x + 2
corrs = []
slopes = []
sds = np.linspace(0.5, 10, 950)
for i in range(950):
    sd = sds[i]
    step_noise = sc.norm.rvs(loc=0, scale=sd, size=30)
    noisy_y = base_y + step_noise
    corrs.append(np.corrcoef(x, noisy_y)[0][1])
    slopes.append(np.cov(x, noisy_y)[0][1] / np.var(x))

pl.scatter(sds, corrs, marker=".", color="green")
pl.title("The Impact of Noise Scale on Empirical Correlation Coefficient")
pl.xticks(np.arange(0.5, 10.5, step=0.5), rotation=90)
pl.xlabel("Scale (Standard Deviation) of Noise Added")
pl.ylabel("Empirical Correlation Coefficient")
pl.yticks(np.arange(-0.1, 1.1, step=0.1))
pl.gcf().subplots_adjust(bottom=0.15)
pl.show()

pl.scatter(sds, slopes, marker=".", color="purple")
pl.title("The Impact of Noise Scale on LSS Slope")
pl.xticks(np.arange(0.5, 10.5, step=0.5), rotation=90)
pl.xlabel("Scale (Standard Deviation) of Noise Added")
pl.ylabel("bLS (LSS Slope)")
pl.yticks(np.arange(0, 11, step=1))
pl.gcf().subplots_adjust(bottom=0.15)
pl.show()