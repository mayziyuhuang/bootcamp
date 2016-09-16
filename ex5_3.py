import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import scipy.optimize
import bootcamp_utils
import ex4_1

def depth_length_model(length, m, a):

    if np.any(np.array(length) < 0):
        raise RuntimeError('length must be positive')
    # if np.any(np.array([m, a]) < 0):
    #     raise RuntimeError('all parameter must be positive')

    return m * length + a

m_guess = 0.5
a_guess = -2
p0 = np.array([m_guess, a_guess])

plt.close()
p, _ = scipy.optimize.curve_fit(depth_length_model, ex4_1.df_f73l, ex4_1.df_f73d, p0=p0)
l_smooth = np.linspace(9, 16, 100)
d_smooth = depth_length_model(l_smooth, *tuple(p))
plt.plot(l_smooth, d_smooth, marker='None', linestyle='-', color='gray')

p, _ = scipy.optimize.curve_fit(depth_length_model, ex4_1.df_s73l, ex4_1.df_s73d, p0=p0)
l_smooth = np.linspace(9, 16, 100)
d_smooth = depth_length_model(l_smooth, *tuple(p))
plt.plot(l_smooth, d_smooth, marker='None', linestyle='-', color='gray')

plt.plot(ex4_1.df_f73l, ex4_1.df_f73d, marker='.', linestyle='none', markersize=10)
plt.plot(ex4_1.df_s73l, ex4_1.df_s73d, marker='.', linestyle='none', markersize=10)

plt.xlabel('beak length (mm)')
plt.ylabel('beak depth (mm)')

plt.show()
