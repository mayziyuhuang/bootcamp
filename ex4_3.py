import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import bootcamp_utils

# write backtrack_steps() function
def backtrack_steps():
    """ computes the number of steps it takes for a random walker"""
    step = 0
    count = 0

    while (step <= 0):
        count += 1
        if np.random.randint(0, 2) == 0:
            step +=1
        else:
            step -=1

    return count

# generate 10000 of backtrack
backtrack = np.empty(100)
for i in range(100):
    backtrack[i] = backtrack_steps()

# plot histogram
plt.figure(1)
_ = plt.hist(backtrack, bins=100, normed=True)
plt.xlabel('backtrack steps')
plt.ylabel('PDF')
#plt.show()

# plot ECDF
plt.figure(2)
x_backtrack, y_backtrack = bootcamp_utils.ecdf(backtrack)
plt.plot(x_backtrack, y_backtrack, marker='.', linestyle='none')
plt.xscale('log')

#plt.show()

# plot complementary cumulative distribution function
plt.figure(3)
plt.loglog(x_backtrack, 1 - y_backtrack, marker='.', linestyle='none')
x_smooth = np.logspace(0.5, 8, 100)
plt.loglog(x_smooth, 1 / np.sqrt(x_smooth))

plt.ylabel('CCDF')
plt.show()
