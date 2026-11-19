import numpy as np

def finite_difference_derivative(coefficients: list, x: float, h: float) -> tuple[float, float, float]:
    """
    Returns the value at x, the value at x plus h, and the estimated slope.
    """
    coef=list(reversed(coefficients))
    y_n=0
    y_n_i=0
    z=len(coef)-1
    z_i=len(coef)-1
    for i in coef:
        y_n=y_n+(x**z)*i
        z=z-1
    for j in coef:
        y_n_i=y_n_i+((x+h)**z_i)*j
        z_i=z_i-1
    return float(y_n),float(y_n_i),float((y_n_i-y_n)/h)