import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

#load the three data sets

wt_data = np.loadtxt('data/wt_lac.csv', skiprows=3, delimiter=',')
q18m_data = np.loadtxt('data/q18m_lac.csv', skiprows=3, delimiter=',')
q18a_data = np.loadtxt('data/q18a_lac.csv', skiprows=3, delimiter=',')

wt_IPTG = wt_data[:,0]
wt_fold = wt_data[:,1]
q18m_IPTG = q18m_data[:,0]
q18m_fold = q18m_data[:,1]
q18a_IPTG = q18a_data[:,0]
q18a_fold = q18a_data[:,1]

#plot
plt.figure(1)
plt.plot(wt_IPTG, wt_fold, marker='.', linestyle='none', markersize=15)
plt.plot(q18m_IPTG, q18m_fold, marker='.', linestyle='none', markersize=15)
plt.plot(q18a_IPTG, q18a_fold, marker='.', linestyle='none', markersize=15)
plt.xscale('log')
plt.xlabel('IPTG (mM)')
plt.ylabel('fold change')

#plt.show()

#function fold_change
def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):

    """compute the fold change"""
    num = RK * (1 + c / KdA)**2
    den = (1 + c / KdA)**2 + Kswitch * (1 + c/ KdI)**2
    fc = (1 + num  / den)**(-1)

    return fc

#plot theoretical fold change
RK_wt = 141.5
RK_q18a = 16.56
RK_q18m = 1328
x = np.logspace(-5, 2, num = 400)
theor_wt = fold_change(x, RK_wt, 0.017, 0.002, 5.8)
theor_q18a = fold_change(x, RK_q18a, 0.017, 0.002, 5.8)
theor_q18m = fold_change(x, RK_q18m, 0.017, 0.002, 5.8)

plt.plot(x, theor_wt, color='gray')
plt.plot(x, theor_q18m, color='gray')
plt.plot(x, theor_q18a, color= 'gray')
plt.title('fold change versus IPTG concentration')
plt.legend(('wt', 'q18m', 'q18a', 'theory_wt', 'theory_q18m', 'theory_q18a'), loc='upper left')


#plt.show()

#data collapse
#calculate Bohr parameter from concentration of IPTG
def bohr_parameter(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):

    """calculate the Bohr concentration from the concentration"""
    num = (1 + c / KdA)**2
    den = (1 + c / KdA)**2 + Kswitch * (1 + c/ KdI)**2
    bohr_data = (-1) * np.log(RK)-np.log(num / den)

    return bohr_data

def fold_change_bohr(bohr_parameter):

    """the fold change as a function of the Bohr parameter"""
    fc_bohr = 1 / (1 + np.exp((-1)*bohr_parameter))
    return fc_bohr

bohr_para = np.linspace(-6, 6, 400)

fc_bohr_data = fold_change_bohr(bohr_para)
plt.figure(2)
plt.plot(bohr_para, fc_bohr_data, color='gray')
#plt.show()

#experimental curve


#plot experimental fold change versus the bohr parameter
wt_bohr = bohr_parameter(wt_IPTG, RK_wt, 0.017, 0.002, 5.8)
q18m_bohr = bohr_parameter(q18m_IPTG, RK_q18m, 0.017, 0.002, 5.8)
q18a_bohr = bohr_parameter(q18a_IPTG, RK_q18a, 0.017, 0.002, 5.8)

plt.plot(wt_bohr, wt_fold, marker='.', linestyle='none', markersize=15)
plt.plot(q18m_bohr, q18m_fold, marker='.', linestyle='none', markersize=15)
plt.plot(q18a_bohr, q18a_fold, marker='.', linestyle='none', markersize=15)
#plt.xscale('log')
plt.xlabel('Bohr parameter')
plt.ylabel('fold change')
plt.title('fold change versus Bohr parameter')
plt.legend(('theory', 'wt', 'q18m', 'q18a'), loc='upper left')
plt.show()
