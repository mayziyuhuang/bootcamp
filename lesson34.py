import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Load the data
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# Rename impact force column
df = df.rename(columns={'impact force (mN)': 'impf'})

# use groupby to select each frog
gb_frog = df.groupby('ID')
mean_impf = gb_frog['impf'].mean()
sem_impf = gb_frog['impf'].sem()

print(mean_impf)
print(sem_impf)

plt.bar(np.arange(4), mean_impf, yerr=sem_impf, ecolor='black',
        tick_label=['I', 'II', 'III', 'IV'], align='center')
plt.ylabel('impact force (mN)')


# use seaborn if you have tidy dataframe, only one line code to make bar graph
sns.barplot(data=df, x='ID', y='impf')
plt.xlabel('')
plt.ylabel('impact force (mN)')
# don't make bar graphs

# use swarm plots
sns.swarmplot(data=df, x='ID', y='impf')
plt.margins(0.02)
plt.xlabel('')
plt.ylabel('impact force (mN)')
