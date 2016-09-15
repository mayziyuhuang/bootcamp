import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import bootcamp_utils
import numba



@numba.jit(nopython=True)
def backtrack_steps():
    """
    Compute the number of steps it takes a 1d random walker starting
    at zero to get to +1.
    """

    # Initialize position and number of steps
    x = 0
    n_steps = 0

    # Walk until we get to positive 1
    while x < 1:
        x += 2 * np.random.randint(0, 2) - 1
        n_steps += 1

    return n_steps


# Stepping time
tau = 0.5 # seconds

# Specify number of samples
n_samples = 10000

# Array of backtrack times
t_bt = np.empty(n_samples)

# Generate the samples
for i in range(n_samples):
    t_bt[i] = backtrack_steps()

# Convert to seconds
t_bt *= tau

plt.figure(1)
_ = plt.hist(t_bt, bins=100, normed=True)
plt.xlabel('time (s)')
plt.ylabel('PDF')


def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1) / len(data)

# Generate x, y values
x, y = ecdf(t_bt)

plt.figure(2)
# Plot CDF from random numbers
plt.semilogx(x, y, '.', markersize=10)

# Clean up plot
plt.margins(y=0.02)
plt.xlabel('time (s)')
plt.ylabel('ECDF')


plt.figure(3)
# Plot the CCDF
plt.loglog(x, 1 - y, '.')

# Plot the asymptotic power law
t_smooth = np.logspace(0.5, 8, 100)
plt.loglog(t_smooth, 1 / np.sqrt(t_smooth))

# Label axes
plt.xlabel('time (s)')
plt.ylabel('CCDF')

plt.show()
