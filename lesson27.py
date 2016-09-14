import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1) / len(data)

# Get bootstrap sample
bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))

# Generate lots of bootstrap replicas
n_reps = 100000
bs_replicates_1975 = np.empty(n_reps)
for i in range(n_reps):
    bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
    bs_replicates_1975[i] = np.mean(bs_sample)

# plt.figure(1)
# _ = plt.hist(bs_replicates_1975, bins=100, normed=True)
# plt.xlabel('mean beak depth (mm)')
# plt.ylabel('PDF')

# Get 95% confidence interval
conf_int_1975 = np.percentile(bs_replicates_1975, [2.5, 97.5])

# for data 2012
# Generate lots of bootstrap replicas
n_reps = 100000
bs_replicates_2012 = np.empty(n_reps)
for i in range(n_reps):
    bs_sample = np.random.choice(bd_2012, replace=True, size=len(bd_2012))
    bs_replicates_2012[i] = np.mean(bs_sample)

# plt.figure(2)
# _ = plt.hist(bs_replicates_2012, bins=100, normed=True)
# plt.xlabel('mean beak depth (mm)')
# plt.ylabel('PDF')

# Get 95% confidence interval
conf_int_2012 = np.percentile(bs_replicates_2012, [2.5, 97.5])




# x_1975, y_1975 = ecdf(bd_1975)
# # x_2012, y_2012 = ecdf(bd_2012)
# x_bs, y_bs = ecdf(bs_sample)
#
# plt.figure(1)
# plt.plot(x_1975, y_1975, marker='.', linestyle='none')
# # plt.plot(x_2012, y_2012, marker='.', linestyle='none')
# plt.plot(x_bs, y_bs, marker='.', linestyle='none', alpha=0.5)
#
# plt.xlabel('beak depth (mm)')
# plt.ylabel('ECDF')
# plt.legend(('1975', 'bootstrap'), loc='lower right')
#

plt.show()
