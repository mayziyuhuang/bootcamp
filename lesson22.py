import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

#plot Airy disk
#The x values we want
x = np.linspace(-15, 15, 400)

#The normalized intensity
norm_I = 4 * (scipy.special.j1(x) / x)**2

plt.plot(x, norm_I)
plt.margins(0.02)
plt.xlabel('$x$')
plt.ylabel('$I(x)/I_0$')
plt.show()

#processing spikes data
data = np.loadtxt('data/retina_spikes.csv', skiprows=2, delimiter=',')

#slice out time and voltage
t = data[:,0]
V = data[:,1]

plt.plot(t, V)
plt.xlabel('t (ms)')
plt.ylabel('V (µV)')
plt.xlim(1395, 1400)
plt.show()
