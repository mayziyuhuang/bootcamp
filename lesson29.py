import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import bootcamp_utils

# Specify parameters
# number of generation
n_gen = 16
# mutation rate, chance to mutate
r = 1e-5
# total number of cells
n_cells = 2**(n_gen -1)


# The adaptive immunity hypothesis
ai_samples = np.random.binomial(n_cells, r, 100000)
counts = np.bincount(ai_samples)
# plt.plot(np.arange(len(counts)), counts, marker='.', linestyle='none')
# #plt.show()

print('AI mean:', np.mean(ai_samples))
print('AI variance:', np.var(ai_samples))
print('AI Fano factor:', np.var(ai_samples / np.mean(ai_samples)))


def draw_random_mutation(n_gen, r):
    """Draw a sample out of the Luria-Delbruck distribution"""
    # initialize number of mutants
    n_mut = 0

    for g in range(n_gen):
        n_mut = 2 * n_mut + np.random.binomial(2**g - 2 * n_mut, r)

    return n_mut


def sample_random_mutation(n_gen, r, n_samples):
    """Sample out of the Luria-Delbruck distribution"""
    # initialize samples
    samples = np.empty(n_samples)

    #draw the samples
    for i in range(n_samples):
        samples[i] = draw_random_mutation(n_gen, r)

    return samples


rm_samples = sample_random_mutation(n_gen, r, 100000)

x_ai, y_ai = bootcamp_utils.ecdf(ai_samples)
x_rm, y_rm = bootcamp_utils.ecdf(rm_samples)

plt.plot(x_ai, y_ai, marker='.', linestyle='none')
plt.plot(x_rm, y_rm, marker='.', linestyle='none')
plt.xscale('log')
plt.show()

print('rm mean:', np.mean(rm_samples))
print('rm variance:', np.var(rm_samples))
print('rm Fano factor:', np.var(rm_samples) / np.mean(rm_samples))
