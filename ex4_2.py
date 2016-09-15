import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import bootcamp_utils


# load the drone weight data as pandas dataframe
df_weight = pd.read_csv('data/bee_weight.csv', comment='#')

# plot ECDFs of drone weight for control and those exposed to pesticide
df_w_control = df_weight.loc[df_weight['Treatment'] == 'Control', 'Weight']
x_w_control, y_w_control = bootcamp_utils.ecdf(df_w_control)

df_w_pesticide = df_weight.loc[df_weight['Treatment'] == 'Pesticide', 'Weight']
x_w_pesticide, y_w_pesticide = bootcamp_utils.ecdf(df_w_pesticide)

plt.figure(1)
plt.plot(x_w_control, y_w_control, marker='.', linestyle='none', markersize=10)
plt.plot(x_w_pesticide, y_w_pesticide, marker='.', linestyle='none', markersize=10)
plt.xlabel('weight')
plt.ylabel('ECDF')
plt.title('drone weight ECDF')
plt.margins(0.02)
plt.legend(('control', 'pesticide'), loc='lower right')

#plt.show()

# calculate the mean drone weight
w_control_mean = np.mean(df_w_control)
w_pesticide_mean = np.mean(df_w_pesticide)

# compute 95% bootstrap confidence intervvals on the mean
reps = bootcamp_utils.draw_bs_reps(df_w_control, np.mean, 10000)
w_control_conf = bootcamp_utils.conf_int(reps, 95)

reps = bootcamp_utils.draw_bs_reps(df_w_pesticide, np.mean, 10000)
w_pesticide_conf = bootcamp_utils.conf_int(reps, 95)

# compute 95% bootstrap confidence intervvals on the median
reps = bootcamp_utils.draw_bs_reps(df_w_control, np.median, 10000)
w_control_conf_median = bootcamp_utils.conf_int(reps, 95)

reps = bootcamp_utils.draw_bs_reps(df_w_pesticide, np.median, 10000)
w_pesticide_conf_median = bootcamp_utils.conf_int(reps, 95)


# load the drone sperm data as pandas dataframe
df_sperm = pd.read_csv('data/bee_sperm.csv', comment='#')

# plot ECDFs of drone weight for control and those exposed to pesticide
df_s_control = df_sperm.loc[df_sperm['Treatment'] == 'Control', 'Quality']
df_s_control = df_s_control.dropna()
x_s_control, y_s_control = bootcamp_utils.ecdf(df_s_control)

df_s_pesticide = df_sperm.loc[df_sperm['Treatment'] == 'Pesticide', 'Quality']
df_s_pesticide = df_s_pesticide.dropna()
x_s_pesticide, y_s_pesticide = bootcamp_utils.ecdf(df_s_pesticide)

plt.figure(2)
plt.plot(x_s_control, y_s_control, marker='.', linestyle='none', markersize=10)
plt.plot(x_s_pesticide, y_s_pesticide, marker='.', linestyle='none', markersize=10)
plt.xlabel('sperm')
plt.ylabel('ECDF')
plt.title('drone sperm ECDF')
plt.margins(0.02)
plt.legend(('control', 'pesticide'), loc='lower right')


# calculate the mean drone weight
s_control_mean = np.mean(df_s_control)
s_pesticide_mean = np.mean(df_s_pesticide)

# compute 95% bootstrap confidence intervvals on the mean
reps = bootcamp_utils.draw_bs_reps(df_s_control, np.mean, 10000)
s_control_conf = bootcamp_utils.conf_int(reps, 95)

reps = bootcamp_utils.draw_bs_reps(df_s_pesticide, np.mean, 10000)
s_pesticide_conf = bootcamp_utils.conf_int(reps, 95)

# compute 95% bootstrap confidence intervvals on the median
reps = bootcamp_utils.draw_bs_reps(df_s_control, np.median, 10000)
s_control_conf_median = bootcamp_utils.conf_int(reps, 95)

reps = bootcamp_utils.draw_bs_reps(df_s_pesticide, np.median, 10000)
s_pesticide_conf_median = bootcamp_utils.conf_int(reps, 95)

plt.show()

# show the confidence interval
print('weight control mean:')
print(w_control_conf)
print('weigth pesticide mean:')
print(w_pesticide_conf)
print('weight control median:')
print(w_control_conf_median)
print('weight pesticide median:')
print(w_pesticide_conf_median)
print('sperm control mean:')
print(s_control_conf)
print('sperm pesticide mean:')
print(s_pesticide_conf)
print('sperm control median:')
print(s_control_conf_median)
print('sperm pesticide median:')
print(s_pesticide_conf_median)
