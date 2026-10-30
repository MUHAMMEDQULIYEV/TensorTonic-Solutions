import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    # Write code here
    x_relu=[]
    for i in x:
        if i>=alpha:
            x_relu.append(i)
        else:
            x_relu.append(i*alpha)
    return np.array(x_relu)