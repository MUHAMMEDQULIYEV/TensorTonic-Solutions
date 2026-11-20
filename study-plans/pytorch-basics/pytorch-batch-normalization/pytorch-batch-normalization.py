import torch

def batch_norm(X: torch.Tensor, gamma: torch.Tensor, beta: torch.Tensor, eps: float = 1e-5) -> torch.Tensor:
    """
    Returns a float32 tensor with the same shape as X.
    """
    mean=X.mean(dim=0)
    var = X.var(dim=0, unbiased=False)
    y_hat=(X-mean)/torch.sqrt(var+eps)
    y=y_hat*gamma+beta
    return y