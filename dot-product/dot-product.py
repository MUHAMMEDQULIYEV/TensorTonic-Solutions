import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    calc=0
    for i in range(len(x)):
        calc=calc+x[i]*y[i]
    return float(calc)