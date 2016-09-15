import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import bootcamp_utils


df_weight = pd.read_csv('data/bee_weight.csv', comment='#')

# Generate ECDFs
x_control, y_control = ecdf(df_weight.loc[df_weight['Treatment']=='Control',
                                        'Weight'])
x_pest, y_pest = ecdf(df_weight.loc[df_weight['Treatment']=='Pesticide',
                                    'Weight'])

# Make plots
plt.plot(x_control, y_control, marker='.', linestyle='none')
plt.plot(x_pest, y_pest, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('weight (mg)')
plt.ylabel('ECDF')
plt.legend(('control', 'pesticide'), loc='lower right')

mean_control = np.mean(df_weight.loc[df_weight['Treatment']=='Control', 'Weight'])
mean_pest = np.mean(df_weight.loc[df_weight['Treatment']=='Pesticide', 'Weight'])

print('Mean control:  ', mean_control, 'mg')
print('Mean pesticide:', mean_pest, 'mg')

def draw_bs_reps(data, func, size=1):
    """Draw bootstrap replicates from a data set."""
    n = len(data)

    # Initialize array of replicates
    reps = np.empty(size)

    for i in range(size):
        # Generate bootstrap sample
        bs_sample = np.random.choice(data, n)

        # Compute replicate
        reps[i] = func(bs_sample)

    return reps

# Draw 100,000 bootstrap reps for both.
bs_reps_control = draw_bs_reps(
        df_weight.loc[df_weight['Treatment']=='Control', 'Weight'], np.mean,
        size=100000)
bs_reps_pest = draw_bs_reps(
        df_weight.loc[df_weight['Treatment']=='Pesticide', 'Weight'], np.mean,
        size=100000)


conf_int_control = np.percentile(bs_reps_control, [2.5, 97.5])
conf_int_pest = np.percentile(bs_reps_pest, [2.5, 97.5])

print('Confidence interval for control:', conf_int_control)
print('Confidence interval for pesticide:', conf_int_pest)


# Load data set
df_sperm = pd.read_csv('data/bee_sperm.csv', comment='#')

# Make ECDF
# Generate ECDFs
x_control, y_control = ecdf(df_sperm.loc[df_sperm['Treatment']=='Control',
                                         'Quality'])
x_pest, y_pest = ecdf(df_sperm.loc[df_sperm['Treatment']=='Pesticide',
                                   'Quality'])

# Make plots
plt.plot(x_control, y_control, marker='.', linestyle='none')
plt.plot(x_pest, y_pest, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('sperm quality')
plt.ylabel('ECDF')
plt.legend(('control', 'pesticide'), loc='lower right')


# Draw 100,000 bootstrap reps for both.
bs_reps_control = draw_bs_reps(
        df_sperm.loc[df_sperm['Treatment']=='Control', 'Quality'].dropna(),
        np.mean,size=100000)
bs_reps_pest = draw_bs_reps(
        df_sperm.loc[df_sperm['Treatment']=='Pesticide', 'Quality'].dropna(),
        np.mean, size=100000)

# Compute and print confidence interval
conf_int_control = np.percentile(bs_reps_control, [2.5, 97.5])
conf_int_pest = np.percentile(bs_reps_pest, [2.5, 97.5])

print('Confidence interval for control:', conf_int_control)
print('Confidence interval for pesticide:', conf_int_pest)


# Draw 100,000 bootstrap reps for both.
bs_reps_control = draw_bs_reps(
        df_sperm.loc[df_sperm['Treatment']=='Control', 'Quality'].dropna(),
        np.median,size=100000)
bs_reps_pest = draw_bs_reps(
        df_sperm.loc[df_sperm['Treatment']=='Pesticide', 'Quality'].dropna(),
        np.median, size=100000)

# Compute and print confidence interval
conf_int_control = np.percentile(bs_reps_control, [2.5, 97.5])
conf_int_pest = np.percentile(bs_reps_pest, [2.5, 97.5])

print('Confidence interval for control:', conf_int_control)
print('Confidence interval for pesticide:', conf_int_pest)
