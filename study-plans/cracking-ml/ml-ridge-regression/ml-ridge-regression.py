import numpy as np

def ridge_regression(X: list, y: list, alpha: float, lr: float, epochs: int) -> tuple:
    """
    Returns the fitted weight list and bias.
    """
    X_arr=np.array(X,dtype=np.float64)
    y_arr=np.array(y,dtype=np.float64)
    n_samples, n_features = X_arr.shape
    weight=np.zeros(n_features)
    bias=0.0
    for i in range(epochs):
        yi=X_arr@weight+bias
        L=(np.sum(yi-y_arr)**2) +np.sum(weight**2)*alpha
        
        dldw = (2 / n_samples) * (X_arr.T @ (yi-y_arr)) + 2 * alpha * weight
        dldb=(2 / n_samples)*np.sum(yi-y_arr)
        weight=weight-dldw*lr
        bias=bias-dldb*lr
    return weight.tolist(), float(bias)
        
