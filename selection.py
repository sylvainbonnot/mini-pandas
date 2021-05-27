from operator import itemgetter
from functools import partial

def get_column(col=0):
    return partial(map,itemgetter(col))

def apply_func_to_first(func):
    return partial(apply_to_first, func)

def drop_n(num=1):
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
