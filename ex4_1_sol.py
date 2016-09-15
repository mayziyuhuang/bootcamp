import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import bootcamp_utils


# Get list of CSV files
csv_list = glob.glob('data/grant*.csv')

# Initialize list of DataFrames
df_list = []

# Load in each sequentially.
for csv_file in csv_list:
    # Read in DataFrame
    df = pd.read_csv(csv_file, comment='#')

    # Place in list
    df_list.append(df)

# Initialize years
years = []
for csv_file in csv_list:
    years.append(int(csv_file[-8:-4]))

# Rename to year
df_list[0] = df_list[0].rename(columns={'yearband': 'year'})

# No worries about Y2K
df_list[0]['year'] += 1900

# Check it out
#df_list[0].head()

for i, df in enumerate(df_list):
    df_list[i]['year'] = np.ones(len(df), dtype=int) * years[i]

def rename_cols(df):
    """Rename columns so all DataFrames have same column headings."""

    # Sniff out the key names from names that are close
    band_key = df.columns[df.columns.str.contains('and')][0]
    species_key = df.columns[df.columns.str.contains('ecies')][0]
    length_key = df.columns[df.columns.str.contains('len')][0]
    depth_key = df.columns[df.columns.str.contains('dep')][0]
    year_key = df.columns[df.columns.str.contains('year')][0]

    # Rename the columns using renaming dictionary
    return df.rename(columns={band_key: 'band',
                              species_key: 'species',
                              depth_key: 'beak depth (mm)',
                              length_key: 'beak length (mm)',
                              year_key: 'year'})


for i, df in enumerate(df_list):
    df_list[i] = rename_cols(df)


df = pd.concat(df_list, axis=0, ignore_index=True)


# Stats about how many birds were measured more than once
print('There were', len(df['band'][df['band'].duplicated()].unique()),
      'birds that were measured more than once.')
print('There were', len(df['band'].unique()), 'total birds measured.')


# Drop all rows with matching year and band (keep first)
df = df.drop_duplicates(subset=['year', 'band'])

df.to_csv('data/grant_complete.csv', index=False)


def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1) / len(data)

# Pull out data for ECDF plotting
bd_fortis = \
    df.loc[(df['species']=='fortis') & (df['year']==1987), 'beak depth (mm)']
bd_scandens = \
  df.loc[(df['species']=='scandens') & (df['year']==1987), 'beak depth (mm)']

bl_fortis = \
    df.loc[(df['species']=='fortis') & (df['year']==1987), 'beak length (mm)']
bl_scandens = \
  df.loc[(df['species']=='scandens') & (df['year']==1987), 'beak length (mm)']

# Set up figure
fig, ax = plt.subplots(2, 1, figsize=(8, 5))

# Plot beak depth ECDFs
x, y = ecdf(bd_fortis)
ax[0].plot(x, y, marker='.', linestyle='none')
x, y = ecdf(bd_scandens)
ax[0].plot(x, y, marker='.', linestyle='none')
ax[0].margins(0.02)

# Plot beak length ECDFs
x, y = ecdf(bl_fortis)
ax[1].plot(x, y, marker='.', linestyle='none')
x, y = ecdf(bl_scandens)
ax[1].plot(x, y, marker='.', linestyle='none')
ax[1].margins(0.02)

# Legends and axis labels, tidying
ax[0].legend(('fortis', 'scandens'), loc='lower right')
ax[0].set_xlabel('beak depth (mm)')
ax[0].set_ylabel('ECDF')
ax[1].set_ylabel('ECDF')
ax[1].set_xlabel('beak length (mm)')
fig.tight_layout(h_pad=3)

# Extract data we want
df_fortis = df[(df['year']==1987) & (df['species']=='fortis')]
df_scandens = df[(df['year']==1987) & (df['species']=='scandens')]

# Plot the result
plt.plot(df_fortis['beak length (mm)'], df_fortis['beak depth (mm)'],
         marker='.', linestyle='None', alpha=0.5)
plt.plot(df_scandens['beak length (mm)'], df_scandens['beak depth (mm)'],
         marker='.', linestyle='None', alpha=0.5)

# Clean up
plt.margins(0.02)
plt.xlabel('beak length (mm)')
plt.ylabel('beak depth (mm)')
plt.legend(('fortis', 'scandens'), loc='upper left')


def plot_beak_data(ax, df, year, legend=False):
    """
    Plot beak length and beak depth data for a given year
    on a given axis.
    """

    # Extract data we want
    df_fortis = df[(df['year']==year) & (df['species']=='fortis')]
    df_scandens = df[(df['year']==year) & (df['species']=='scandens')]


    # Plot the result
    ax.plot(df_fortis['beak length (mm)'], df_fortis['beak depth (mm)'],
            marker='.', linestyle='None', alpha=0.5)
    ax.plot(df_scandens['beak length (mm)'], df_scandens['beak depth (mm)'],
            marker='.', linestyle='None', alpha=0.5)

    # Clean up
    ax.margins(0.02)
    ax.set_xlabel('beak length (mm)', fontsize=12)
    ax.set_ylabel('beak depth (mm)', fontsize=12)
    ax.set_title(str(year), fontsize=14)
    if legend:
        ax.legend(('fortis', 'scandens'), loc='upper left')

    return ax


# Plots playout
fig, ax = plt.subplots(2, 3, figsize=(8, 5), sharex=True, sharey=True)

# Which axes to use
ax_inds = ((0,0), (0, 1), (0,2), (1,0), (1, 1))

# Loop through years and make plots
for i, year in enumerate(years):
    if i == 0:
        legend = True
    else:
        legend=False

    _ = plot_beak_data(ax[ax_inds[i]], df, year, legend=legend)

# Tidy up
ax[1, 2].axis('off')
fig.tight_layout()
