import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

df_big_force = df.loc[df['impact force (mN)'] > 1000, :]

df.loc[(df['date'] == '2013_05_27') & (df['ID'] == 'III'), :]

df.loc[:, ['impact force (mN)', 'adhesive force (mN)']]

df.loc[df['ID']=='I', ['impact force (mN)', 'adhesive force (mN)']]

plt.plot(df['impact force (mN)'], df['adhesive force (mN)'], marker='.', linestyle='none')

#plt.clf() : clean out the figure

# Use pandas dataframes to plot
df.plot(x='total contact area (mm2)', y='adhesive force (mN)', kind='scatter')

# correlation
df.corr()

# Rename the impact force column
df = df.rename(columns={'impact force (mN)': 'impf'})

df['impf'] = df.impf
