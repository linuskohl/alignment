from typing import List
from .helpers import validate_frequency_vector

def berry_mielke(V: List[int]) -> float:
    """
        From: Berry, K.J., Mielke, P.W.: Indices of ordinal variation (1992)
        Args:
            F(List[int]): Frequency vector
        Returns:
            float:
        Raises:
            Exception: Invalid frequency vector
    """
    validate_frequency_vector(V)
    N = sum(V)
    k = len(V)  # nr. categories
    # The following loop is equivalent to:
    # t  = sum from i=1 to k-1 ( sum from j = i+1 to k (ni*nj*(i-j)) )
    # ni, nj = cell counts; i, j = values of categories
    t = sum([sum([V[i] * V[j] * (j - i) for j in range(i + 1, k)]) for i in range(0, k - 1)])
    # Tmax not defined with odd numbers;
    if N % 2 == 1:  # If N is odd, use (N^2-1)*(k-1)/4
        Tmax = (N ** 2 - 1) * (k - 1) / 4
    else:
        Tmax = N ** 2 * (k - 1) / 4
    iov = t / Tmax

    return iov
