# coding=utf8

from functools import wraps
from flask import request
from werkzeug.contrib.cache import MemcachedCache


_cache = MemcachedCache(
    ['127.0.0.1:11211'],
)


def cache(key, timeout=5*60):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            rv = _cache.get(key)
            if rv is not None:
                return rv
            rv = f(*args, **kwargs)
            _cache.set(key, rv, timeout=timeout)
            return rv
        return decorated_function
    return decorator
