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

    return diameter


A = np.array([[6.7, 1.3, 0.6, 0.7],
              [0.1, 5.5, 0.4, 2.4],
              [1.1, 0.8, 4.5, 1.7],
              [0.0, 1.5, 3.4, 7.5]])

b = np.array([1.1, 2.3, 3.3, 3.9])

#print row 1 of A
#index 1 of A
#A[1,:]
#print columns 1 and 3 of A
#A[:, [1,3]]
#print the values of every entry in A that is greater than 2
#A[A > 2]
#print the diagonal of A using the np.diag() function
#np.diag(A)

#solve A . x = b
#x = np.linalg.solve(A, b)
#np.dot(A, x)
#np.transpose(A)
#np.linalg.inv(A)

#B = np.ravel(A)
#np.reshape(B, (4,4))
#np.reshape(B, (number of rows, number of columns))
