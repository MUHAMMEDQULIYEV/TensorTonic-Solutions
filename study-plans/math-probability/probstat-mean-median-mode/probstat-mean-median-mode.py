import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns mean, median, and mode as Python floats in a dictionary.
    """
    x_arr=np.array(x)
    mean=np.mean(x_arr)
    median=np.median(x_arr)
    values, counts=np.unique(x_arr,return_counts=True)
    mode=values[np.argmax(counts)]
    return {"mean": float(mean), "median": float(median), "mode": float(mode)}
    