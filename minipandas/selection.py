"""
Simple iterator functions to mimick pandas functions
"""

from operator import itemgetter
from functools import partial

def dummy():
    """
    Dummy function
    .. code-block:: python

    >>> a = 2
    >>> print(a)
    2
    
    >>> b = ['wow',
    ...      'eee']
    >>> print(b)
    ['wow', 'eee']

    |
    """
    return True

def get_column(col=0):
    return partial(map,itemgetter(col))

def apply_func_to_first(func):
    return partial(apply_to_first, func)

def drop_n(num=1):
    """
    drop first elements
    ```
    def double(x):
        return 2*x
    
    >>> double(3)
    >>> 6
    ```
    
    """
    return partial(drop, num)

def unzip(tuple_gen):
    fst, snd = zip(*tuple_gen)
    return fst, snd

def to_array(iterable):
    return np.array(iterable)

def apply_fst(func):
    def result(*args):
        fst, *rest = args
        return func(fst), *rest
    return result

def apply_snd(func):
    def result(*args):
        fst, snd, *rest = args
        return fst, func(snd), *rest
    return result  
