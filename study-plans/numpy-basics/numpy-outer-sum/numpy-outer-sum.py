import numpy as np

def outer_sum(a: list, b: list) -> np.ndarray:
    """
    Returns an (m, n) float64 array of pairwise sums.
    """
    a_rr=np.array(a,dtype=np.float64)
    b_arr=np.array(b,dtype=np.float64)
    return np.add.outer(a_rr,b_arr)
