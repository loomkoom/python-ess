from random import *
from math import *


def proxy_pi(req_tries=1000):
  """
    Calculate an approximation of the number PI.
    - The accuracy of the returned approximation normally
      grows with an increasing number of requested tries.
    - However, the resulting approximation will not
      always be the same for invocations involving the
      same number of requested tries.
  """

  nb_hits = 0
  nb_tries = 0

  while nb_tries < req_tries:

    x = random() * 2 - 1.0
    y = random() * 2 - 1.0

    if sqrt(x * x + y * y) <= 1.0:
      nb_hits += 1

    nb_tries += 1

  return 4.0 * nb_hits / nb_tries



print(proxy_pi())
print(proxy_pi(100000))
print(proxy_pi(10000000))
