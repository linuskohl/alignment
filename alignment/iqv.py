from typing import List


def iqv(V: List[int]) -> float:
    """
    Calculate Index of Qualitative Variation
    A simple index of qualitative variation
    Gibbs and Poston (1975)
    Args:
        F(List[int]): Vector
    Returns:
        float: iqv
    """
    I = len(V)
    n = sum(V)
    iqv = (I/(I-1))*(1-sum((V[i]/n)**2 for i in range(0,I)))

    return iqv
