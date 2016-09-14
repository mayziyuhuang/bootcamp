import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

#practice 3: computing and plotting a ECDFs

#load data sets
xa_high = np.loadtxt('data/xa_high_food.csv', comments = '#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments = '#')

#function ecdf(data)
def ecdf(data):

    """a function to compute the ECDF"""
    x = np.sort(data)
    y = np.arange(0, 1, 1/len(data))

    return x, y

x_high, y_high = ecdf(xa_high)
plt.plot(x_high, y_high, marker='.', linestyle='none', markersize=15, alpha=0.5)

x_low, y_low = ecdf(xa_low)
plt.plot(x_low, y_low, marker='.', linestyle='none', markersize=15, alpha=0.5)

plt.xlabel('cross sectional area')
plt.ylabel('ECDF')
plt.legend(('high', 'low'), loc='lower right')

plt.show()
