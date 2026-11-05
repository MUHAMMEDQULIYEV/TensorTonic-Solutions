import numpy as np

def activation_functions(x: float, activation: str) -> list:
    """
    Returns the activation value and analytical derivative.
    """
    result = []
    if activation == "relu":
        f = max(0, x)
        f_der = np.where(x > 0, 1, 0)
        result.append(f)
        result.append(f_der)
    elif activation == "leaky_relu":
        f=np.where(x>0,x,0.01*x)
        f_der = np.where(x > 0, 1, 0.01)
        result.append(f)
        result.append(f_der)
    elif activation == "sigmoid":
        f = 1/(1+ np.exp(-x))
        f_der = f * (1 - f)
        result.append(f)
        result.append(f_der)
    elif activation == "tanh":
        f = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
        f_der = 1 - f ** 2
        result.append(f)
        result.append(f_der)
    elif activation == "gelu":
        c = np.sqrt(2 / np.pi)
        u = c * (x + 0.044715 * x ** 3)
        t = np.tanh(u)
        f = 0.5 * x * (1 + t)
        f_der = 0.5 * (1 + t) + 0.5 * x * (1 - t ** 2) * c * (1 + 3 * 0.044715 * x ** 2)
        result.append(f)
        result.append(f_der)
    else:
        f=x*(1/(1+ np.exp(-x)))
        f_der=1/(1+ np.exp(-x)) +x*(1/(1+ np.exp(-x)))*(1-(1/(1+ np.exp(-x))))
        result.append(f)
        result.append(f_der)
    return result