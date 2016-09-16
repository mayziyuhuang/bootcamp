import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import bootcamp_utils

# load files into separate Pandas DataFrames
df_1973 = pd.read_csv('data/grant_1973.csv', comment='#')
df_1975 = pd.read_csv('data/grant_1975.csv', comment='#')
df_1987 = pd.read_csv('data/grant_1987.csv', comment='#')
df_1991 = pd.read_csv('data/grant_1991.csv', comment='#')
df_2012= pd.read_csv('data/grant_2012.csv', comment='#')

# change the name of the yearband column of the 1973 data to year
# year format is four digits
df_1973 = df_1973.rename(columns={'yearband': 'year'})
df_1973 = df_1973.replace('73', '1973')

# add a year column to other four DataFrames
df_1975['year'] = '1975'
df_1987['year'] = '1987'
df_1991['year'] = '1991'
df_2012['year'] = '2012'

# change the column names ['band', 'species', 'beak length (mm)', 'beak depth (mm)', 'year']
df_1973 = df_1973.rename(columns={'beak length':'beak length (mm)', 'beak depth':'beak depth (mm)'})
df_1973 = df_1973[['band', 'species', 'beak length (mm)', 'beak depth (mm)', 'year']]
df_1975 = df_1975.rename(columns={'Beak length, mm':'beak length (mm)', 'Beak depth, mm':'beak depth (mm)'})
df_1975 = df_1975[['band', 'species', 'beak length (mm)', 'beak depth (mm)', 'year']]
df_1987 = df_1987.rename(columns={'Beak length, mm':'beak length (mm)', 'Beak depth, mm':'beak depth (mm)'})
df_1987 = df_1987[['band', 'species', 'beak length (mm)', 'beak depth (mm)', 'year']]
df_1991 = df_1991.rename(columns={'blength':'beak length (mm)', 'bdepth':'beak depth (mm)'})
df_1991 = df_1991[['band', 'species', 'beak length (mm)', 'beak depth (mm)', 'year']]
df_2012 = df_2012.rename(columns={'blength':'beak length (mm)', 'bdepth':'beak depth (mm)'})
df_2012 = df_2012[['band', 'species', 'beak length (mm)', 'beak depth (mm)', 'year']]

# concatenate the dataframes into a single dataframes
df = pd.concat((df_1973, df_1975, df_1987, df_1991, df_2012), axis=0, ignore_index=True)

# save the tidy dataframes in a CSV document
df.to_csv('data/grant_complete.csv', index=False)


# let's delete only duplicate birds from the same year from the DataFrame.
df['Du'] = df.loc[(df['year'] == '1973') | (df['year'] == '1975') | (df['year'] == '1987') | (df['year'] == '1991') | (df['year'] == '2012'),:].duplicated('band')

df = df[df.Du != True]
df = df.drop('Du', axis=1)
df.to_csv('data/grant_complete_noduplicate.csv', index=False)

# plot and ECDF of beak depths of fortis in 1987
# and also of scandens in 1987
df_f87d = df.loc[(df['year'] == '1987') & (df['species'] == 'fortis'), 'beak depth (mm)']
x_f87d, y_f87d = bootcamp_utils.ecdf(df_f87d)

df_s87d = df.loc[(df['year'] == '1987') & (df['species'] == 'scandens'), 'beak depth (mm)']
x_s87d, y_s87d = bootcamp_utils.ecdf(df_s87d)

plt.figure(1)
plt.plot(x_f87d, y_f87d, marker='.', linestyle='none', markersize=10)
plt.plot(x_s87d, y_s87d, marker='.', linestyle='none', markersize=10)
plt.xlabel('beak depths (mm)')
plt.ylabel('ECDF')
plt.title('beak depths ECDF in 1987')
plt.margins(0.02)
plt.legend(('fortis', 'scandens'), loc='lower right')

# plot and ECDF of beak lengths of fortis in 1987
# and also of scandens in 1987
df_f87l = df.loc[(df['year'] == '1987') & (df['species'] == 'fortis'), 'beak length (mm)']
x_f87l, y_f87l = bootcamp_utils.ecdf(df_f87l)

df_s87l = df.loc[(df['year'] == '1987') & (df['species'] == 'scandens'), 'beak length (mm)']
x_s87l, y_s87l = bootcamp_utils.ecdf(df_s87l)

plt.figure(2)
plt.plot(x_f87l, y_f87l, marker='.', linestyle='none', markersize=10)
plt.plot(x_s87l, y_s87l, marker='.', linestyle='none', markersize=10)
plt.xlabel('beak lengths (mm)')
plt.ylabel('ECDF')
plt.title('beak lengths ECDF in 1987')
plt.margins(0.02)
plt.legend(('fortis', 'scandens'), loc='lower right')


# plot beak depth versus beak length for 1987 data for both fortis and scandens
plt.figure(3)
plt.plot(df_f87d, df_f87l, marker='.', linestyle='none', markersize=10, color='blue')
plt.plot(df_s87d, df_s87l, marker='.', linestyle='none', markersize=10, color='red')
plt.xlabel('beak depth (mm)')
plt.ylabel('beak length (mm)')
plt.title('beak depth versus beak length in 1987')
#plt.margins(0.02)
plt.xlim(6, 13)
plt.ylim(8, 17)
plt.legend(('fortis', 'scandens'), loc='lower right')

# plot figure 3 for all years
# 1973
plt.figure(4)
df_f73d = df.loc[(df['year'] == '1973') & (df['species'] == 'fortis'), 'beak depth (mm)']
df_s73d = df.loc[(df['year'] == '1973') & (df['species'] == 'scandens'), 'beak depth (mm)']
df_f73l = df.loc[(df['year'] == '1973') & (df['species'] == 'fortis'), 'beak length (mm)']
df_s73l = df.loc[(df['year'] == '1973') & (df['species'] == 'scandens'), 'beak length (mm)']

plt.plot(df_f73d, df_f73l, marker='.', linestyle='none', markersize=10, color='blue')
plt.plot(df_s73d, df_s73l, marker='.', linestyle='none', markersize=10, color='red')
plt.xlabel('beak depth (mm)')
plt.ylabel('beak length (mm)')
plt.title('beak depth versus beak length in 1973')
#plt.margins(0.02)
plt.xlim(6, 13)
plt.ylim(8, 17)
plt.legend(('fortis', 'scandens'), loc='lower right')

# 1975
plt.figure(5)
df_f75d = df.loc[(df['year'] == '1975') & (df['species'] == 'fortis'), 'beak depth (mm)']
df_s75d = df.loc[(df['year'] == '1975') & (df['species'] == 'scandens'), 'beak depth (mm)']
df_f75l = df.loc[(df['year'] == '1975') & (df['species'] == 'fortis'), 'beak length (mm)']
df_s75l = df.loc[(df['year'] == '1975') & (df['species'] == 'scandens'), 'beak length (mm)']

plt.plot(df_f75d, df_f75l, marker='.', linestyle='none', markersize=10, color='blue')
plt.plot(df_s75d, df_s75l, marker='.', linestyle='none', markersize=10, color='red')
plt.xlabel('beak depth (mm)')
plt.ylabel('beak length (mm)')
plt.title('beak depth versus beak length in 1975')
#plt.margins(0.02)
plt.xlim(6, 13)
plt.ylim(8, 17)
plt.legend(('fortis', 'scandens'), loc='lower right')

# 1991
plt.figure(6)
df_f91d = df.loc[(df['year'] == '1991') & (df['species'] == 'fortis'), 'beak depth (mm)']
df_s91d = df.loc[(df['year'] == '1991') & (df['species'] == 'scandens'), 'beak depth (mm)']
df_f91l = df.loc[(df['year'] == '1991') & (df['species'] == 'fortis'), 'beak length (mm)']
df_s91l = df.loc[(df['year'] == '1991') & (df['species'] == 'scandens'), 'beak length (mm)']

plt.plot(df_f91d, df_f91l, marker='.', linestyle='none', markersize=10, color='blue')
plt.plot(df_s91d, df_s91l, marker='.', linestyle='none', markersize=10, color='red')
plt.xlabel('beak depth (mm)')
plt.ylabel('beak length (mm)')
plt.title('beak depth versus beak length in 1991')
#plt.margins(0.02)
plt.xlim(6, 13)
plt.ylim(8, 17)
plt.legend(('fortis', 'scandens'), loc='lower right')

# 2012
plt.figure(7)
df_f12d = df.loc[(df['year'] == '2012') & (df['species'] == 'fortis'), 'beak depth (mm)']
df_s12d = df.loc[(df['year'] == '2012') & (df['species'] == 'scandens'), 'beak depth (mm)']
df_f12l = df.loc[(df['year'] == '2012') & (df['species'] == 'fortis'), 'beak length (mm)']
df_s12l = df.loc[(df['year'] == '2012') & (df['species'] == 'scandens'), 'beak length (mm)']

plt.plot(df_f12d, df_f12l, marker='.', linestyle='none', markersize=10, color='blue')
plt.plot(df_s12d, df_s12l, marker='.', linestyle='none', markersize=10, color='red')
plt.xlabel('beak depth (mm)')
plt.ylabel('beak length (mm)')
plt.title('beak depth versus beak length in 2012')
#plt.margins(0.02)
plt.xlim(6, 13)
plt.ylim(8, 17)

plt.legend(('fortis', 'scandens'), loc='lower right')
#%plt.show()
