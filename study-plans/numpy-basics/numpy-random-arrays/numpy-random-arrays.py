import numpy as np

def generate_random_array(shape: list, kind: str, seed: int) -> np.ndarray:
    """
    Returns a seeded 2D float64 random array with the requested shape.
    """
    rng=np.random.default_rng(seed=seed)
    if kind == "uniform":
        arr = rng.uniform(size=shape)   # samples from [0, 1)
    else:
        arr = rng.normal(size=shape)    # mean 0, std 1
    return arr.astype(np.float64)
        