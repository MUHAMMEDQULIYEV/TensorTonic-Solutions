import numpy as np

def dropout(X: list, mask: list, drop_prob: float, mode: str) -> list:
    """
    Returns the train-mode dropout result or unchanged test input.
    """
    x_arr=np.array(X)
    mask_arr=np.array(mask)
    if mode=="train":
        return (x_arr*mask_arr)/(1-drop_prob)
    else:
        return x_arr
