from typing import List
from .helpers import dsquared


def blair_lacy(V: List[int]) -> float:
    """
    Measure of concentration,  "l" squared, Blair & Lacy 2000
    Args:
        F(List[int]): Frequency vector
    Returns:
        float:
    """
    d = dsquared(V) ** 0.5
    k = len(V)
    dmax = ((k - 1) / 4) ** 0.5

    return (d / dmax)
