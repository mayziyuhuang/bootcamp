import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')
import skimage.filters
import skimage.io
import skimage.measure
import skimage.segmentation
import skimage.morphology

def segmentation(data, cutoffsize):
    """segmentation function"""
    # load images
    im = skimage.io.imread(data)

    # apply gussian blur
    im_blur = skimage.filters.gaussian(im, 50.0)

    # subtract the background
    im_float = skimage.img_as_float(im)
    im_sub = im_float - im_blur

    # # correct for hot or bad pixel in an image
    # selem = skimage.morphology.square(3)
    # im_filt = skimage.filters.median(im_sub, selem)

    # apply otsu threshold
    thresh = skimage.filters.threshold_otsu(im_sub)
    im_seg = im_sub < thresh

    # remove objects near the image border
    im_seg = skimage.segmentation.clear_border(im_seg, buffer_size=5)

    # label binary image; background kwarg says value in im_bw to be background
    im_labeled, n_labels = skimage.measure.label(im_seg, background=0, return_num=True)


    # extract region props
    ip_dist = 0.063
    im_props = skimage.measure.regionprops(im_labeled)

    # filtered black and white image
    im_bw = np.copy(im_labeled) > 0

    # define cutoff size
    cutoff = cutoffsize

    #areas = np.array([im_props.area for prop in im_props])

    for prop in im_props:
        if prop.area < cutoff:
            im_bw[im_labeled==prop.label] = 0


    area_filt_lab = skimage.measure.label(im_bw > 0)

    #plt.imshow(area_filt_lab, cmap=plt.cm.Spectral_r)

    return area_filt_lab
