import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Specify parameter
alpha = 1
beta = 0.2
delta = 0.3
gamma = 0.8

# Set the time step
delta_t = 0.001

# Make an array of time points
t = np.arange(0, 60, delta_t)

# Make an array to store the number of foxes, and rabbits
r = np.empty_like(t)
f = np.empty_like(t)

# Initial number of foxes and rabbits
r[0] = 10
f[0] = 1


# Write a for loop to keep updating n as time goes on
for i in range(1, len(t)):
    r[i] = r[i-1] + delta_t * (alpha * r[i-1] - beta * f[i-1] * r[i-1])
    f[i] = f[i-1] + delta_t * (delta * f[i-1] * r[i-1] - gamma * f[i-1])

#plot the animals number growth
plt.plot(t, r)
plt.plot(t, f)
plt.xlabel('time (a.u.)')
plt.ylabel('population')
plt.legend(('rabbits', 'foxes'))

# plt.plot(t, r)
# plt.plot(t, f)
# plt.margins(0.02)
# plt.xlabel('time')
# plt.ylabel('number of foxes and rabbits')
# plt.legend(('rabbits', 'foxes'), loc='upper right')
plt.show()
