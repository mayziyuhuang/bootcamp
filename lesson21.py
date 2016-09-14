import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#set matplotlib rc file
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

#load in data
xa_high = np.loadtxt('data/xa_high_food.csv', comments = '#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments = '#')

low_min = np.min(xa_low)
low_max = np.max(xa_low)
high_min = np.min(xa_high)
high_max = np.max(xa_high)
global_min = np.min([low_min, high_min])
global_max = np.max([low_max, high_max])

#Make bin boundaries
bins = np.arange(global_min-50, global_max+51, 50)

#plot data as histogram
_ = plt.hist(xa_low, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)


#add axis labels
plt.xlabel('Cross-sectional area (µm$^2$)')
plt.ylabel('count frequency')
#if you want to make the label horizontal for presentation
#plt.ylabel('count', rotation = 'horizontal')
#add a legend
plt.legend(('low', 'high'), loc='upper right')


_ = plt.hist(xa_high, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)

#add axis labels
plt.xlabel('Cross-sectional area (µm$^2$)')
plt.ylabel('count frequency')
#if you want to make the label horizontal for presentation
#plt.ylabel('count', rotation = 'horizontal')
#add a legend
plt.legend(('low', 'high'), loc='upper right')


#save the figure
plt.savefig('lesson21_plot_1_egg_histogram.svg', bbox_inches='tight')

plt.show()
