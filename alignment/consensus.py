from math import log2
from statistics import mean
from .helpers import expand, validate_frequency_vector
from typing import List


def consensus(F: List[int]) -> float:
    """ Calculate Tastle and Wierman’s measure of consensus
        The function returns the measure of consensus.
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
    if max(F) == sum(F):
        return 1
    s = sum(F)
    P = [b / s for b in F]
    pos = range(1, len(F) + 1)
    mx = mean(expand(F))
    dx = max(pos) - min(pos)
    cns = 1 + sum([a * b for a, b in zip(P, [(log2(1 - abs(p - mx) / dx)) for p in pos])])

    return cns
