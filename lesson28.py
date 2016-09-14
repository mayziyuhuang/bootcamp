import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import bootcamp_utils

# practice 1: write a function to draw bootstrap replicates
def draw_bs_reps(data, func, size=1):
    """Draw bootstrap replicates from data"""

    n = len(data)
    reps = np.empty(100000)
    for i in range(100000):
        bs_sample = np.random.choice(data, replace=True, size=n)
        reps[i] = func(bs_sample)

    return reps

# practice 2: plot ECDFs of bootstrap samples
bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
x_1975, y_1975 = bootcamp_utils.ecdf(bd_1975)

plt.plot(x_1975, y_1975, marker='.', color='blue', linestyle='none')

for i in range(100):
    bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
    x_bs, y_bs = bootcamp_utils.ecdf(bs_sample)
    plt.plot(x_bs, y_bs, marker='.', color='blue', alpha=0.01, linestyle='none')



plt.xlabel('beak depth (mm)')
plt.ylabel('ECDF')
plt.margins(0.02)
plt.show()
