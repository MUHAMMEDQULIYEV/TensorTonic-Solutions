import numpy as np
import math
def softmax_regression(X: list, y: list, num_classes: int, lr: float, n_iters: int) -> tuple:
    """
    Returns the fitted weight matrix and bias vector.
    """
    x_arr=np.array(X,dtype=np.float64)
    y_arr=np.array(y,dtype=np.int64)
    Y=np.zeros((x_arr.shape[0],num_classes))
    Y[np.arange(x_arr.shape[0]), y_arr] = 1
    Y_arr=np.array(Y)
    weight=np.zeros((x_arr.shape[1],num_classes))
    bias=np.zeros(num_classes)
    
    for _ in range(n_iters):
        z=x_arr@weight+bias
        m=np.max(z,axis=1,keepdims=True)
        p=np.exp(z-m)/np.sum(np.exp(z-m),keepdims=True,axis=1)
        dldw=(1/x_arr.shape[0])*x_arr.T@(p-Y_arr)
        dldb=(1/x_arr.shape[0])*np.sum((p-Y_arr),axis=0)
        weight=weight-dldw*lr
        bias=bias-dldb*lr
    return np.round(weight,4),np.round(bias,4)
        