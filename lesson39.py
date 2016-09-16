import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')
import skimage.filters
import skimage.io
import skimage.measure
import skimage.segmentation
import skimage.morphology

# load images
phase_im = skimage.io.imread('data/HG105_images/noLac_phase_0004.tif')

# show image
plt.imshow(phase_im, cmap=plt.cm.viridis)

# the upper pixel are darker than lower ones (background)


# apply gussian blur
im_blur = skimage.filters.gaussian(phase_im, 50.0)
plt.imshow(im_blur, cmap=plt.cm.viridis)
plt.close()

# subtract the background
# convert the median filtered phase image to float
phase_float = skimage.img_as_float(phase_im)
phase_sub = phase_float - im_blur

plt.figure()
plt.imshow(phase_float, cmap=plt.cm.viridis)
plt.title('original')

plt.figure()
plt.imshow(phase_sub, cmap=plt.cm.viridis)
plt.title('subtraction')


# apply otsu threshold
thresh = skimage.filters.threshold_otsu(phase_sub)
seg = phase_sub < thresh
plt.close('all')
plt.imshow(seg, cmap=plt.cm.Greys_r)
# we have some little dots in the background
# also we can not recognize different bacteria or label

# label the bacteria
seg_lab, num_cells = skimage.measure.label(seg, background=0, return_num=True)
plt.close()
plt.imshow(seg_lab, cmap=plt.cm.Spectral_r)

# find each cells
#plt.imshow(seg_lab == 1)

# how to choose only the bacteria
# use the area
# extract region of each bacteria
ip_dist = 0.063
props = skimage.measure.regionprops(seg_lab)
# props[0].area: show the area of first object
# the background is labeled as 0

# less than 150 pixel is not a bacteria
areas = np.array([prop.area for prop in props])
cutoff = 300

im_cells = np.copy(seg_lab) > 0
# make a copy and make it white and black
for prop in props:
    if prop.area < cutoff:
        im_cells[seg_lab==prop.label] = 0
# for i, _ in enumerate(areas):
#     if areas[i] < cutoff:
#         im_cells[seg_lab==props[i].label] = 0

area_filt_lab = skimage.measure.label(im_cells > 0)
plt.figure()
plt.imshow(area_filt_lab, cmap=plt.cm.Spectral_r)

plt.figure()
plt.imshow(im_cells)


plt.show()
