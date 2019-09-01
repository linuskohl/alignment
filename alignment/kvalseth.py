from typing import List
from .berry_mielke import berry_mielke


def kvalseth(V: List[int]) -> float:
    """
    This function calculates Kvalseth's COV, a measure of dispersion
    based on linear Euclidean distances. It is based on th IOV measure,
    implemented as BerryMielke. This function follows the presentation by
    Blair and Lacy 2000.
    Args:
        V(List[int]): Frequency vector
    Returns:
        float: COV, as cited in Blair & Lacy 2000
    """
    COV = 1 - (1 - berry_mielke(V)) ** 0.5

    return (COV)
