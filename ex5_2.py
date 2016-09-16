import glob
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')
import skimage.filters
import skimage.io
import skimage.measure
import skimage.segmentation
import skimage.morphology
import lesson40_a
import scipy.optimize

# load in the series of images
im_list_phase = glob.glob('data/HG105_images/noLac_phase_*.tif')
im_phase = []
for file in im_list_phase:
    im_phase.append(skimage.io.imread(file))

im_list_FITC = glob.glob('data/HG105_images/noLac_FITC_*.tif')
im_FITC = []
for file in im_list_FITC:
    im_FITC.append(skimage.io.imread(file))

im_seg = []
for i in range(9):
    thresh = skimage.filters.threshold_otsu(im_phase[i])
    seg = im_phase[i] < thresh
    im_seg.append(seg)

im_intensity = []
for i in range(9):
    im_labeled, n_labels = skimage.measure.label(im_seg[i], background=0, return_num=True)
    props = skimage.measure.regionprops(im_labeled, intensity_image=im_FITC[i])
    intensity = np.array([prop.mean_intensity for prop in props])
    im_intensity.append(intensity)

total_intensity = np.empty(9)
for i in range(9):
    total_intensity[i] = np.sum(im_intensity[i])
