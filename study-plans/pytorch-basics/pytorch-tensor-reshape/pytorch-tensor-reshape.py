import torch

def reshape_tensor(x: torch.Tensor, op: str) -> torch.Tensor:
    """
    Returns the reshaped float32 tensor, including a scalar tensor after a complete squeeze.
    """
    if op=="view":
        return torch.view(x)
    elif op=="flatten":
        return torch.flatten(x)
    elif op=="squeeze":
        return torch.squeeze(x)
    elif op=="unsqueeze":
        return torch.unsqueeze(x)
    else:
        return torch.transpose(x,0,1)
