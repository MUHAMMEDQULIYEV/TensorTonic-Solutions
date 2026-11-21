import numpy as np

def adam_step(
    param: list,
    grad: list,
    m: list,
    v: list,
    t: int,
    lr: float = 1e-3,
    beta1: float = 0.9,
    beta2: float = 0.999,
    eps: float = 1e-8,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
        Returns (param_new, m_new, v_new) as NumPy arrays.
    """
    # Write code here
    param_arr=np.array(param)
    grad_arr=np.array(grad)
    m_arr=np.array(m)
    v_arr=np.array(v)
    mtb=m_arr
    vtb=v_arr
    mtb=beta1*mtb +(1-beta1)*grad_arr
    vtb=beta2*vtb +(1-beta2)*grad_arr**2
    mtb_hat=mtb/(1-beta1**t)
    vtb_hat=vtb/(1-beta2**t)
    param_arr=param_arr-lr*(mtb_hat/((np.sqrt(vtb_hat)+eps)))
    return param_arr,mtb,vtb