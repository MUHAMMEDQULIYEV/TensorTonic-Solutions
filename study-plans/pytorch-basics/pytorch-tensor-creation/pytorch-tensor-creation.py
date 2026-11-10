import torch

def create_tensor(method: str, shape: list, value: float = 0.0) -> torch.Tensor:
    """
    Returns a float32 tensor with the requested shape.
    """
    if method=="ones":
        k=torch.ones(shape,dtype=torch.float32)
    elif method=="zeros":
        k=torch.zeros(shape,dtype=torch.float32)
    else:
        k=torch.full(shape,value,dtype=torch.float32)

    return k
