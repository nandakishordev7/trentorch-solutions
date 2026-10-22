import numpy as np


def trace(A):
    return np.diag(A).sum()
    pass


def trace_of_product(A, B):
    return np.sum(A * B.T)
    pass
