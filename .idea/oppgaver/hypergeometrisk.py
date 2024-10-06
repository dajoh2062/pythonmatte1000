import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import hypergeom

# Parameters
M = 140  # Number of successes in the population
N = 640  # Population size
n = 8  # Number of draws

# Values for x (number of successes in the sample)
x = np.arange(0, min(n, M) + 1)

# Probabilities for each value of x
probabilities = hypergeom.pmf(x, N, M, n)

# Plotting
plt.bar(x, probabilities, align='center', alpha=0.7)
plt.xlabel('Number of successes in the sample')
plt.ylabel('Probability')
plt.title(f'Hypergeometric Distribution\n(M={M}, N={N}, n={n})')
plt.xticks(x)
plt.grid(True)
plt.show()
