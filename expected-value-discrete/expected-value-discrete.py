import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    x1=np.asarray(x,dtype=float)
    p1=np.asarray(p,dtype=float)

    return np.dot(x1,p1)
    pass