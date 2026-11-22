import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Write code here
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return np.sort(eigenvalues)