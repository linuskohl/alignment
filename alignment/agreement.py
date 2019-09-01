import math
from typing import List
from .helpers import pattern_vector


def pattern_agreement(P: List[int], old: bool = False) -> float:
    """
    Calculates agreement A from a pattern vector
    Args:
        P(List[int]): Pattern vector
        old(boolean): Use old Unimodality algorithm (passed on)
    Returns:
        float: Agreement from pattern vector
     """
    if max(P) > 1:
        raise Exception(
            "Error: Input is not a pattern vector (only 0 and 1 are allowed).")
    # This error should never occur unless the function is called directly.
    K = len(P)  # nr. of categories
    # Counting triplets
    TDU = 0  # count = 0
    TU = 0  # count = 0
    for i in range(0, K - 2):  # repeat for position A
        for j in range(i + 1, K - 1):  # repeat for position B
            for m in range(j + 1, K):  # repeat for position C
                if (P[i] == 1 and P[j] == 0 and P[
                    m] == 1): TDU += 1  # 101 pattern, bimodal (TDU)
                if (P[i] == 1 and P[j] == 1 and P[
                    m] == 0): TU += 1  # 110 pattern, unimodal (TU)
                if (P[i] == 0 and P[j] == 1 and P[
                    m] == 1): TU += 1  # 011 pattern, unimodal (TU)
                # all other patterns are not counted
    if old == True:
        # using the old algorithm (outlined in endnotes)
        U = (TU - TDU) / (TU + TDU)
    else:
        # normal case: U as in equation (2) on p.332
        U = ((K - 2) * TU - (K - 1) * TDU) / ((K - 2) * (TU + TDU))
    S = sum(P)  # number of non-empty
    A = U * (1 - (S - 1) / (K - 1))  # calculating agreement A
    if A == math.nan:
        A = 0  # lack of agreement, defined as 0
    if sum(P) == 1:
        A = 1  # only one value, defined as 1

    return (A)


def agreement(V: List[int], old: bool = False) -> float:
    """
    Calculates agreement A for multiple layers
    Params:
        V(List[int]): Frequency vector
        old(boolean): Use old Unimodality algorithm (passed on)
    Returns:
        float: Agreement from pattern vector
     """
    if len(V) < 3:
        print("Warning: length of vector < 3, agreement A is not defined.")
        return math.nan
    if min(V) < 0:
        raise Exception("Error: negative values found in frequency vector.")
    AA = 0  # begin with empty agreement A (overall), prepare
    k = len(V)  # number of categories
    N = sum(V)  # number of cases
    R = V  # remainder
    for i in range(0, k):  # repeat for each layer i
        P = pattern_vector(R)  # get the pattern vector for layer i
        if max(P) == 0:  # remainder is empty, all layers are analyzed
            break
        A = pattern_agreement(P, old)  # agreement A for layer i
        m = min(filter(None, R))  # get non-zero minimum of remainder R
        L = [p * m for p in P]  # layer i with the values
        w = sum(L) / N  # weight of layer i
        AA = AA + w * A  # adding agreement of layer i to overall agreement
        R = [r - l for r, l in zip(R, L)]  # new reminder

    return AA
