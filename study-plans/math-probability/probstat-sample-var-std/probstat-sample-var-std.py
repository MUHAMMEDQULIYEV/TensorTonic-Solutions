import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns sample variance and standard deviation as Python floats.
    """
    X_arr=np.array(x,dtype=np.float64)
    std_dev = np.std(X_arr,ddof=1)
    variance = np.var(X_arr,ddof=1)
    return {"variance": variance, "std_dev": std_dev}