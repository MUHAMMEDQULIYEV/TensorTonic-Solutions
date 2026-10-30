import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    x_arr=np.array(x)
    result = {
    "variance": float(np.var(x_arr,ddof=1)),
    "standard_deviation":float(np.std(x_arr,ddof=1))}
    return result
    