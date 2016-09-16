import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')
import skimage.filters
import skimage.io
import skimage.measure
import skimage.segmentation
import skimage.morphology

import lesson40_a

im = lesson40_a.segmentation('data/HG105_images/noLac_phase_0004.tif', 150)
im_intensity = skimage.io.imread('data/HG105_images/noLac_FITC_0004.tif')
im_props = skimage.measure.regionprops(im, intensity_image=im_intensity)

# store mean and total fluorescence intensity_image
data_array = np.empty(len(im_props))
for i in range(len(im_props)):
    data_array[i] = im_props[i].mean_intensity

# plot histogram
_ = plt.hist(data_array)
plt.xlabel('Intensity')
plt.ylabel('count')

plt.show()
