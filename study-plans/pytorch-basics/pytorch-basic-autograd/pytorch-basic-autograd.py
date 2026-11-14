import torch

def compute_gradient(values: torch.Tensor) -> torch.Tensor:
    """
    Returns a float32 gradient tensor with the same shape as values.
    """
    
    x = values.detach().to(torch.float32).requires_grad_(True)
    y=(x*x*x+x*2).sum()
    y.backward()
    return x.grad