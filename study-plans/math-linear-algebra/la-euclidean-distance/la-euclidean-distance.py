import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a float.
    """
    x_arr=np.array(x,dtype=np.float64)
    y_arr=np.array(y,dtype=np.float64)
    k=np.sqrt(np.sum((x_arr-y_arr)**2))
    return float(k)