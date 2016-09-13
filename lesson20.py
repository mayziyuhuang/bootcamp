#practice 1
import numpy as np

np.linspace(0, 10, 11)

np.arange(11)

#practice 2
xa_high = np.loadtxt('data/xa_high_food.csv', comments = '#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments = '#')

def xa_to_diameter(xa):

    """convert an array of cross-sectional areas to diameters with commensurate units."""

    #compute diameter from area
    diameter = np.sqrt(xa * 4 / np.pi)

    return diamter
