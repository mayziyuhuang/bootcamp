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
    y = np.arange(0, 1, 1/len(data))

    return x, y
