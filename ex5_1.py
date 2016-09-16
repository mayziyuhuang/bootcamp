import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
#sns.set_style('dark')
import skimage.filters
import skimage.io
import skimage.measure
import skimage.segmentation
import skimage.morphology
import lesson40_a
import scipy.optimize

# mass
# m(t) = m_0 * e**(rt)
# mass proportional to area
# look up the readme file to find out the time

# load in the series of images
im_list = glob.glob('data/bacterial_growth/bacillus*.tif')
im = []
for file in im_list:
    im.append(skimage.io.imread(file))
# store it as a tuple
im = tuple(im)


# segment the images
im_seg = [None] * len(im)
for i, image in enumerate(im):
    thresh = skimage.filters.threshold_otsu(image)
    im_seg[i] = image > thresh


# get area data
pixel_area = 0.0645**2
im_area = []
for i in range(55):
    im_labeled, n_labels = skimage.measure.label(im_seg[i], background=0, return_num=True)
    props = skimage.measure.regionprops(im_labeled)
    areas = np.array([prop.area for prop in props])
    im_area.append(areas)

total_area = np.empty(len(im_seg))
for i in range(55):
    total = np.sum(im_area[i])
    total_area[i] = total * pixel_area

# plot a growth curve
# time between frames is 15 minutes
time = 0.25 * np.arange(len(im_seg))
plt.plot(time, total_area, marker='.', linestyle='none')
plt.xlabel('time (minutes)')
plt.ylabel('area')

def cell_growth_model(time, log_A_0, log_tau):

    if np.any(np.array(time) < 0):
        raise RuntimeError('depth must be positive')
    if np.any(np.array([log_A_0, log_tau]) < 0):
        raise RuntimeError('all parameter must be positive')

    return np.exp(log_A_0) * np.exp(time / np.exp(log_tau))


p0 = np.log(np.array([4.0, 4.0]))

log_p, _ = scipy.optimize.curve_fit(cell_growth_model, time, total_area, p0=p0)
time_smooth = np.linspace(0, time.max(), 200)
a_smooth = cell_growth_model(time_smooth, *tuple(log_p))

plt.plot(time_smooth, a_smooth, marker='None', linestyle='-')
print("""
b_0 = {0:.2f} sq. µm
  τ = {1:.2f} hours
""".format(*tuple(np.exp(log_p))))


plt.show()
