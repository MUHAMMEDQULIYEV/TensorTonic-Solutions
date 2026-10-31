import numpy as np

def create_filled_array(shape: list, kind: str) -> np.ndarray:
    """
    Returns a 2D float64 array of zeros or ones with the requested shape.
    """
    if kind=="zeros":
        arr=np.zeros(shape,dtype=np.float64)
    else:
        arr=np.ones(shape,dtype=np.float64)
    return arr
