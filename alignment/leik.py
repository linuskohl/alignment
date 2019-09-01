from itertools import accumulate
from typing import List


def leik(V: List[int]) -> float:
    """
    Leik (1966) A Measure of Ordinal Consensus
    Args:
        F(List[int]): Frequency vector
    Returns:
        float: ordinal consensus
    """
    n = sum(V)
    m = len(V)
    P = [v / n for v in V]  # calculate percentages
    R = list(accumulate(P))  # cumulative frequency distribution
    SDi = [R[x] if R[x] <= .5 else 1 - R[x] for x in range(0, m)]
    maxSDi = 0.5 * (m - 1)  # maximum possible SDi given n
    D = sum(SDi) / maxSDi  # ordinal dispersion; standardized

    return (D)
