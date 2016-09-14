#lesson 24 practice 5
import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)
import bootcamp_utils

xa_high = np.loadtxt('data/xa_high_food.csv', comments = '#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments = '#')
x_high, y_high = bootcamp_utils.ecdf(xa_high)
plt.plot(x_high, y_high, marker='.', linestyle='none', markersize=15, alpha=0.5)

x_low, y_low = bootcamp_utils.ecdf(xa_low)
plt.plot(x_low, y_low, marker='.', linestyle='none', markersize=15, alpha=0.5)

plt.xlabel('cross sectional area')
plt.ylabel('ECDF')
plt.legend(('high', 'low'), loc='lower right')


x = np.linspace(1600, 2500, 400)
cdf_theor_low = scipy.stats.norm.cdf(x, loc=np.mean(xa_low), scale=np.std(xa_low))
cdf_theor_high = scipy.stats.norm.cdf(x, loc=np.mean(xa_high), scale=np.std(xa_high))

plt.plot(x, cdf_theor_low, color='gray')
plt.plot(x, cdf_theor_high, color='gray')

plt.show()
