## Birinci Versiya

---

'''

import numpy as np

def original_and_clipped(data: list, row_idx: int, lo: float, hi: float) -&gt; np.ndarray:

    """

    Returns a (2, n) float64 array: original row, then clipped row.

    """

    arr=np.array(data,dtype=np.float64)

    k=np.clip(arr[row_idx],lo,hi)

    return np.stack([arr[row_idx],k])

'''
## 
,Ikinci esil versiya



import numpy as np

def original_and_clipped(data: list, row_idx: int, lo: float, hi: float) -&gt; np.ndarray:

    """

    Returns a (2, n) float64 array: original row, then clipped row.

    """

    a = np.array(data, dtype=np.float64)

    original = a[row_idx].copy():burda datani copy edir ki esil datani deyismesin

    return np.stack([original, np.clip(original, lo, hi)])