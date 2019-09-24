from math import log2
from .helpers import validate_frequency_vector
from typing import List


def consensus(F: List[int]) -> float:
    """
    Calculate Tastle and Wierman’s measure of consensus.
    The measure of consensus is based on the Shannon entropy.
    Tastle, W., and M. Wierman. 2007. Consensus and dissention:
    A measure of ordinal dispersion. International Journal of Approximate
    Reasoning 45(3): 531-545.
    Args:
        F(List[int]): Frequency vector
    Returns:
        float: Consensus. 1 on perfect uniformity,
               0 on perfect bimodality (lack of agreement).
    Raises:
        Exception: Invalid frequency vector
    """
    validate_frequency_vector(F)

    # When all observations are the same, consensus is not defined but definition as 1

    m = sum(F)
    n = len(F)
    X = range(1, n + 1)
    if max(F) == m:
        return 1
    P = [x / m for x in F]
    dX = max(X) - min(X)
    mx = sum(P[i] * X[i] for i in range(0, n))
    cns = 1 + sum(P[i] * log2(1 - (abs(X[i] - mx) / dX)) for i in range(0, n))

    return cns
