import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    np_arr=np.array(x)
    np_arr_exp= 1/(1+np.exp(-np_arr))
    return np_arr_exp