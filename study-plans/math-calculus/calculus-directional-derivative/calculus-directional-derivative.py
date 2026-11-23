import numpy as np

def directional_derivative_analysis(w: list, v: list) -> dict:
    """
    Returns gradient and directional steepest-descent data.
    """
    
    w_arr=np.array(w)
    v_arr=np.array(v)
    v_arr=v_arr/np.sqrt(np.sum(v_arr**2))
    grad = np.array([2*w_arr[0], 6*w_arr[1]])
    digrad=np.dot(grad,v_arr)
    steepgrad=np.sqrt(np.sum(grad**2))
    if steepgrad==0.0:
        l=[0,0]
    else:
        l=[-grad[0]/steepgrad,-grad[1]/steepgrad]
    return {"gradient": grad.tolist(), "directional_derivative":float(digrad) , "steepest_descent_direction":l, "max_descent_rate": -float(steepgrad)}