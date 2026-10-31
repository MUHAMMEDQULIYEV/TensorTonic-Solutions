import numpy as np

def create_sequence(start: float, stop: float, param: float, kind: str) -> np.ndarray:
    """
    Returns a 1D float64 array containing the requested sequence.
    """
    if kind=="arange":
        arr=np.arange(start=start,stop=stop,step=param)
    else:
        arr=np.linspace(start=start,stop=stop,num=param)
    arr=np.array(arr,dtype=np.float64)
    return arr