import numpy as np
from collections import Counter




def knn_classifier(X_train: list, y_train: list, X_test: list, k: int) -> list:
    """
    Returns one predicted label for each test row.
    """
    X_train=np.array(X_train)
    X_test=np.array(X_test)
    y_train = np.array(y_train)
    pred=[]
    for x in X_test:
            dists = np.sqrt(np.sum((X_train - x) ** 2, axis=1))
            k_ids=np.argsort(dists)[:k]
            k_labels=y_train[k_ids]
            values,count=np.unique(k_labels,return_counts=True)
            pred.append(values[np.argmax(count)])
    return pred
            
