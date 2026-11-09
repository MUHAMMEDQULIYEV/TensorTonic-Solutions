import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    """
    Returns the error as a float.
    """
    # Write code here
    y_pred_arr=np.array(y_pred)
    y_true_arr=np.array(y_true)
    return (np.sum((y_pred_arr-y_true_arr)**2))/len(y_pred_arr)