import numpy as np
def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))
    
def logistic_regression(X: list, y: list, lr: float, n_iters: int) -> tuple:
    """
    Returns the fitted weight list and bias.
    """
    X_arr=np.array(X)
    y_arr=np.array(y)
    weight=np.zeros(X_arr.shape[1])
    bias=0.0
    for step in range(n_iters):
        z=X@weight+bias
        p=_sigmoid(z)
        loss = -np.mean(y_arr * np.log(p) + (1 - y_arr) * np.log(1 - p))
        DlDW = X_arr.T @ (p - y_arr) / X_arr.shape[0]          
        DLDb = np.mean(p - y_arr)
        weight=weight-lr*DlDW
        bias=bias-lr*DLDb
    return weight,bias