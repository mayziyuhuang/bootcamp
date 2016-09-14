import numpy as np
import scipy.integrate

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)


# Specify parameters
alpha = 1
beta = 0.2
delta = 0.3
gamma = 0.8
delta_t = 0.001
t = np.arange(0, 60, delta_t)

# Make arrays to store rabbit and fox populations
r = np.empty_like(t)
f = np.empty_like(t)

# Set initial conditions
r[0] = 10
f[0] = 1

# Write a for loop to keep updating r and f as time goes on
for i in range(1, len(t)):
    r[i] = r[i-1] + delta_t * (alpha * r[i-1] - beta * f[i-1] * r[i-1])
    f[i] = f[i-1] + delta_t * (delta * f[i-1] * r[i-1] - gamma * f[i-1])

plt.plot(t, r)
plt.plot(t, f)
plt.xlabel('time (a.u.)')
plt.ylabel('population')
plt.legend(('rabbits', 'foxes'))
plt.show()
