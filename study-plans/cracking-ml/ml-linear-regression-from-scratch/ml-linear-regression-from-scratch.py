import numpy as np

def linear_regression_from_scratch(X: list, y: list, lr: float, epochs: int) -> tuple:
    """
    Returns the fitted weight list and bias.
    """
    x_arr=np.array(X,dtype=np.float64)
    y_arr=np.array(y,dtype=np.float64)
    bias=0.0
    n=x_arr.shape[0]
    weight=np.zeros(x_arr.shape[1])
    for i in range(epochs):
        yi=x_arr@weight+bias
        L=(2/n)*(yi-y_arr)
        dw = x_arr.T @ L
        db = np.sum(L)
        weight=weight-lr*dw
        bias=bias-lr*db
    return weight,bias
        
