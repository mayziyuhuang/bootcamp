import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# for image processing
import skimage.io
import skimage.exposure
import skimage.morphology
import skimage.filters


# load image
phase_im = skimage.io.imread('data/bsub_100x_phase.tif')
cfp_im = skimage.io.imread('data/bsub_100x_cfp.tif')

# show image
# plt.imshow(phase_im)
# cmap = color map
# don't use jet cmap
#plt.imshow(phase_im, cmap=plt.cm.viridis)

# plot histogram data
hist_phase, bins_phase = skimage.exposure.histogram(phase_im)
plt.plot(bins_phase, hist_phase)
plt.xlabel('pixel value')
plt.ylabel('count')

# apply threshold values (the peak from the histogram is the background)
# choose the intensity below the peak to choose only bacteria
thresh = 325
im_phase_thresh = phase_im < thresh
plt.close()

with sns.axes_style('dark'):
    plt.imshow(im_phase_thresh, cmap=plt.cm.Greys_r)


# show the cfp image
with sns.axes_style('dark'):
    plt.imshow(cfp_im, cmap=plt.cm.viridis)

# slice down the image where it is damaged
plt.close()
with sns.axes_style('dark'):
    plt.imshow(cfp_im[150:250, 450:550]/cfp_im.max(), cmap=plt.cm.viridis)

# use median filter
# make the structuring element
# selem = skimage.morphology.disk(1)
# plt.imshow(selem)
# plt.imshow(selem, interpolation='nearest')

selem = skimage.morphology.square(3)
cfp_filt = skimage.filters.median(cfp_im, selem)
with sns.axes_style('dark'):
    plt.imshow(cfp_filt, cmap=plt.cm.viridis)


# plot histogram data
plt.close()
hist_cfp, bins_cfp = skimage.exposure.histogram(cfp_filt)
plt.plot(bins_cfp, hist_cfp)
plt.xlabel('pixel value')
plt.ylabel('count')

thresh_cfp = 120
im_cfp_thresh = cfp_filt > thresh_cfp
plt.close()

# otsu's method
with sns.axes_style('dark'):
    plt.imshow(im_cfp_thresh, cmap=plt.cm.Greys_r)

with sns.axes_style('dark'):
    plt.imshow(im_phase_thresh, cmap=plt.cm.Greys_r)



plt.show()
