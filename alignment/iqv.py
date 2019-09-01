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
    k = len(V)
    tot = sum(V)
    perc = [(v / tot) * 100 for v in V]
    result = (k * (100 ** 2 - sum([p ** 2 for p in perc])) / (100 ** 2 * (k - 1))) * 100

    return result
