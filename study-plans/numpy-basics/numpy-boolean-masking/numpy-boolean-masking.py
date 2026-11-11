import numpy as np

def row_summary(data: list, threshold: float) -> np.ndarray:
    """
    Returns a float64 array of shape (3, m, n): mask, any-row, all-row.
    """
    arr=np.array(data,dtype=np.float64)
    mask=np.where(arr>threshold,1.0,0.0)
    
    mask_any=np.any(arr>threshold,axis=1,keepdims=True)
    mask_any_where=np.where(mask_any,arr,0.0)
    
    mask_all=np.all(arr>threshold,axis=1,keepdims=True)
    mask_all_where=np.where(mask_all,arr,0.0)
    return np.stack([mask, mask_any_where, mask_all_where], axis=0)
    
    
    
