from typing import List

def mrq (V: List[int])->float:
  """
  Polarization index (Montalvo and Reynal-Querol 2005)
  Args:
      F(List[int]): Frequency vector
  Returns:
      float: polarization
  """
  z = len(V)
  s = sum(V)
  # standardizing frequency vector if necessary
  if sum(V) != 1:
        V = [z / s for z in V]
  return 4 * sum([z ** 2 * (1-z) for z in V[0:z]])
