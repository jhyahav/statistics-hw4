import scipy.stats as sc
import numpy as np

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