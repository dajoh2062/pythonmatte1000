import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Parameters
n = 8      # Number of trials
p = 140 / 640  # Probability of success

# Values for x (number of successes in the trials)
x = np.arange(0, n + 1)

# Probabilities for each value of x
probabilities = binom.pmf(x, n, p)

# Plotting
plt.bar(x, probabilities, align='center', alpha=0.7)
plt.xlabel('Number of successes in the trials')
plt.ylabel('Probability')
plt.title(f'Binomial Distribution\n(n={n}, p={p:.2f})')
plt.xticks(x)
plt.grid(True)
plt.show()
