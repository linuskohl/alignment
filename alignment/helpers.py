from typing import List


def validate_frequency_vector(F):
    """ Validates a frequency vector
        Args:
            F(List[int]): Frequency vector
        Raises:
            Exception: Invalid frequency vector
    """
    if min(F) < 0:
        raise Exception("Negative values found in frequency vector.")
    if not all(isinstance(b, int) for b in F):
        raise Exception(
            "Error: not all values are whole numbers; not a frequency vector; multiply by 100?")


def expand(F: List[int]) -> List[int]:
    """ Converts frequency vector in a population vector
        Args:
            F(List[int]): Frequency vector
        Returns:
            List[int]: The expanded vector
        Raises:
            Exception: Invalid frequency vector
    """
    validate_frequency_vector(F)

    k = len(F)
    D = []
    for i in range(0, k):
        D.extend([i + 1] * F[i])

    return D


def pattern_vector(F: List[int]) -> List[int]:
    """ Converts a frequency vector into a pattern vector
        Args:
            F(List[int]): Frequency vector
        Returns:
            List[int]: Pattern vector
        Raises:
            Exception: Invalid frequency vector
    """
    validate_frequency_vector(F)

    k = len(F)  # number of categories
    P = []  # prepare empty P
    for i in range(0, k):
        x = 0 if F[i] == 0 else 1
        P.append(x)

    return (P)
