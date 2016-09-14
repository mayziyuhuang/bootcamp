import numpy as np
import pandas as pd

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# extract impact time of all impacts that had an adhesive strength of magnitude greater than 2000 pa
df.loc[df['adhesive strength (Pa)'] > 2000, 'impact time (ms)']

# extract the impact force and adhesive force for frog II
df.loc[df['ID'] == 'II', ['impact force (mN)', 'adhesive force (mN)']]

# c) Extract the adhesive force and the time the frog pulls on the target for juvenile frogs (Frogs III and IV).
df.loc[(df['ID'] == 'III') | (df['ID'] == 'IV'), ['adhesive force (mN)', 'time frog pulls on target (ms)']]

# and: using & (shift + 7)
# or: using | (shift + \)


# practice 2: The power of groupby()
# extract all frog 1 impact forces and compute the mean

df.loc[df['ID'] == 'I', 'impact force (mN)']
mean_I = df.loc[df['ID'] == 'I', 'impact force (mN)'].mean()
mean_II = df.loc[df['ID'] == 'II', 'impact force (mN)'].mean()
mean_III = df.loc[df['ID'] == 'III', 'impact force (mN)'].mean()
mean_IV = df.loc[df['ID'] == 'IV', 'impact force (mN)'].mean()
mean_array = np.array([mean_I, mean_II, mean_III, mean_IV])


# using groupby()
# We only want ID's and impact forces, so slice those out
df_impf = df.loc[:, ['ID', 'impact force (mN)']]

# Make a GroupBy object
grouped = df_impf.groupby('ID')

# Apply the np.mean function to the grouped object
df_mean_impf = grouped.apply(np.mean)

# Look at the new DataFrame
df_mean_impf

df_ana_impf = grouped.agg([np.mean, np.median, np.std])

# function computes the coefficient of variation
def coeff_of_var(data):
    """calculate coefficient of variation"""
    cv = data.apply(np.std) / data.apply(np.mean)

    return cv

df_cv_impf = coeff_of_var(grouped)

df_af = df.loc[:, ['ID', 'adhesive force (mN)']]
grouped_af = df_af.groupby('ID')
df_ana_af = grouped_af.agg([np.mean, np.median, np.std])
df_cv_af = coeff_of_var(grouped_af)

df_frog = pd.concat((df_ana_impf, df_cv_impf, df_ana_af, df_cv_af), axis = 1)
df_frog = df_frog.rename(columns={'impact force (mN)': '(impact force (mN), cv)', 'adhesive force (mN)':'(adhesive force (mN), cv)'})
