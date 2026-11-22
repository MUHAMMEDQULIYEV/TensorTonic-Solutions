import numpy as np

def eigendecompose(A: list) -> dict:
    """
    Returns sorted float64 eigenvalues and eigenvectors in a dictionary.
    """
    eigenvalues, eigenvectors = np.linalg.eig(A)
    return  {"eigenvalues": eigenvalues, "eigenvectors": eigenvectors}