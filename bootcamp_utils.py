"""bootcamp utils: a collection of the functions in bootcamp"""
import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

def ecdf(data):

    """a function to compute the ECDF"""
    x = np.sort(data)
    y = np.arange(1, len(x)+1) / len(x)

    return x, y


def draw_bs_reps(data, func, size=1):
    """Draw bootstrap replicates from data"""

    n = len(data)
    reps = np.empty(100000)
    for i in range(100000):
        bs_sample = np.random.choice(data, replace=True, size=n)
        reps[i] = func(bs_sample)

    return reps

def conf_int(data, percentile):
    """ calculate confident interval"""
    
    lower_percen = (100 - percentile) / 2
    higher_percen = 100 - lower_percen

    return np.percentile(data, [lower_percen, higher_percen])
