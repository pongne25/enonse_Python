 #POKO FINI

import operator
from functools import reduce


def product(s):
    if s:

        return reduce(operator.mul, s)





print(product([ 1, 22, 3]))
