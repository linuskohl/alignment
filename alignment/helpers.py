from typing import List


def validate_frequency_vector(V: List[int])->None:
    """
    Validates a frequency vector
    Args:
        V(List[int]): Frequency vector
    Raises:
        Exception: Invalid frequency vector
    """
    if min(V) < 0:
        raise Exception("Negative values found in frequency vector.")
    if not all(isinstance(b, int) for b in V):
        raise Exception(
            "Error: not all values are whole numbers; not a frequency vector; multiply by 100?")


def expand(V: List[int]) -> List[int]:
    """
    Converts frequency vector in a population vector
    Args:
        V(List[int]): Frequency vector
    Returns:
        List[int]: The expanded vector
    Raises:
        Exception: Invalid frequency vector
    """
    validate_frequency_vector(V)

    k = len(V)
    D = []
    for i in range(0, k):
        D.extend([i + 1] * V[i])

    return D


def pattern_vector(V: List[int]) -> List[int]:
    """
    Converts a frequency vector into a pattern vector
    Args:
        V(List[int]): Frequency vector
    Returns:
        List[int]: Pattern vector
    Raises:
        Exception: Invalid frequency vector
    """
    validate_frequency_vector(V)

    k = len(V)  # number of categories
    P = []  # prepare empty P
    for i in range(0, k):
        x = 0 if V[i] == 0 else 1
        P.append(x)

    return (P)


def dsquared(V: List[int]) -> float:
    """
    Calculate ordinal concentration
    According to Blair & Lacy 2000
    Args:
        F(List[int]): Frequency vector
    Returns:
        float: ordinal concentration
    """
    k = len(V)  # number of categories
    n = sum(V)  # number of cases
    V = [v / n for v in V]  # standardizing
    # from 1 to k-1(Fi -.5)^2
    dsq = sum([(sum(V[0:x]) - 0.5) ** 2 for x in range(1, k)])

    return (dsq)
