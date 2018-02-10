import numpy as np
from scipy import sparse

# This is a 2d numpy array on a diagonal of ones and zeroes everywhere else
eye = np.eye(5)
print("Numpy array with sparse :\n{}".format(eye))

## Convert the numpy array to a scipy sparse matrix in compressed sparse row 
## format
# only the non zero entries are stored now

sparse_matrix = sparse.csr_matrix(eye)
print("scipy sparse Compressed Sparse Row (CSR) matrix:\n{}".format(sparse_matrix))

## Different types using different formats
## This one uses COOrdinate format
data = np.ones(5)
row_indices = np.arange(5)
column_indices = np.arange(5)
eye_coo = sparse.coo_matrix((data, (row_indices, column_indices)))
print("scipy sparse COOrdinate (COO) format : \n{}".format(eye_coo))

print("\n\nscipy is installed by the way.")