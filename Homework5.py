import functools
from collections import OrderedDict


class LruCacheus:

    def __init__(self, maxsize):
        self.maxsize = maxsize

    def lru_try(self):

        def decorator(func):
            cache = OrderedDict()

            @functools.wraps(func)
            def wrapped(fargs, *args):
                try:
                    key = fargs
                except TypeError:
                    key = args

                try:
                    result = cache.pop(key)
                    wrapped.hits += 1
                except KeyError:
                    wrapped.misses += 1
                    result = func(fargs, *args)

                cache[key] = result

                if len(cache) >= self.maxsize:
                    cache.popitem()

                return result

            def cache_info():
                print("Our cache: ", cache, "Our hits: ", wrapped.hits, "Misses: ", wrapped.misses)

            def cache_clear():
                cache.clear()
                print(cache)

            wrapped.hits = 0
            wrapped.misses = 0
            wrapped._cache_info = cache_info
            wrapped._cache_clear = cache_clear

            return wrapped

        return decorator
    
    lru = LruCacheus(4)

@lru.lru_try()
def letsgo(a):
    if isinstance(a, tuple):
        mynewtup = tuple([i*10 for i in a])
        return mynewtup

    return a*10

letsgo((10,20))
letsgo(20)
letsgo(30)
letsgo(20)
letsgo._cache_info()
letsgo._cache_clear()