import torch

def compute_loss(pred: torch.Tensor, target: torch.Tensor, method: str, delta: float = 1.0) -> float:
    """
    Returns the mean loss as a Python float.
    """
    if method=="mse":
        loss_fn=torch.nn.MSELoss()
        return float(loss_fn(pred,target))
    elif method=="cross_entropy":
        loss_fn=torch.nn.CrossEntropyLoss()
        return float(loss_fn(pred,target))
    else:
        loss_fn=torch.nn.HuberLoss(reduction="mean",delta=delta)
        return loss_fn(pred,target).item()