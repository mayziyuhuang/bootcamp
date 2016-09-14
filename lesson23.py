import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

#practice 1: Axes with loggarithmic scale
data = np.loadtxt('data/collins_switch.csv', skiprows=2, delimiter=',')

iptg = data[:,0]
gfp = data[:,1]

# plt.figure(1)
# plt.plot(iptg, gfp, marker='.', linestyle='none', markersize=20)
# plt.xlabel('IPTG (mM)')
# plt.ylabel('normalized GFP')
#
# plt.figure(2)
# plt.loglog(iptg, gfp, marker='.', linestyle='none')
# plt.xlabel('IPTG (mM)')
# plt.ylabel('normalized GFP')

# plt.figure(3)
# plt.semilogx(iptg, gfp, marker='.', linestyle='none')
# plt.xlabel('IPTG (mM)')
# plt.ylabel('normalized GFP')
# plt.ylim(-0.05, 1.0)
# plt.xlim(0.0009, 11)

# plt.figure(4)
# plt.semilogy(iptg, gfp, marker='.', linestyle='none')
# plt.xlabel('IPTG (mM)')
# plt.ylabel('normalized GFP')
# plt.show()
#mark all the lines you want to be comments, and use command+/

#practice 2:plots with error bars
sem = data[:,2]
plt.errorbar(iptg, gfp, yerr=sem, marker='.', linestyle='none', markersize=10)
plt.xscale('log')
plt.xlabel('IPTG (mM)')
plt.ylabel('normalized GFP')
plt.ylim(-0.08, 1.2)
plt.xlim(0.0009, 11)
plt.show()
