from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    mean=np.mean(np.array(x,dtype=np.float64))
    median=np.median(np.array(x,dtype=np.float64))
    counts = Counter(np.array(x,dtype=np.float64).ravel())

    # 2. Extract the single most common item
    # .most_common(1) returns a list of tuples: [(value, count)]
    mode, count = counts.most_common(1)[0]
    return {"mean":float(mean),"median":float(median),"mode":float(mode)}