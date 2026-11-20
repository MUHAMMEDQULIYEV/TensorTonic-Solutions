import pandas as pd

def create_dataframe(data: dict) -> dict:
    """
    Returns a dictionary with data, shape [rows, columns], and ordered column  names.
    """
    
    return{"data":data,"shape":list(pd.DataFrame(data).shape),"columns":list(pd.DataFrame(data).columns)}
