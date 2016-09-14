import bootcamp_utils
import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# # Generate sorted random numbers
# x = np.sort(np.random.random(size=100000))
#
# # Generate y-axis for CDF
# y = np.arange(1, len(x)+1) / len(x)
#
# # Plot CDF from random numbers (for plotting purposes, only plot 100 points)
# plt.plot(x[::1000], y[::1000], marker='.', linestyle='none', markersize=10)

x = np.random.random(size=10000)

x_ecdf, y_ecdf = bootcamp_utils.ecdf(x)


plt.plot(x_ecdf[::100], y_ecdf[::100], marker='.', linestyle='none', markersize=10)
plt.plot([0, 1], [0, 1], 'k-')
plt.show()
