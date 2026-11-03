import numpy as np

def perceptron(X: list, y: list, lr: float = 0.1, epochs: int = 100) -> tuple:
    """
    Returns the trained weight list and bias.
    """
    X_arr=np.array(X,dtype=np.float64)
    y_arr=np.array(y,dtype=np.float64)
    w=np.zeros(X_arr.shape[1])
    B=0.0
    for i in range(epochs):
        for i in range(X_arr.shape[0]):
            z=X_arr[i]@w+B   
            y_hat = 1.0 if z >= 0.0 else 0.0
            w=w+lr*(y_arr[i]-y_hat)*X_arr[i]
            B=B+lr*(y_arr[i]-y_hat)

    return w.tolist(), B
    
        
