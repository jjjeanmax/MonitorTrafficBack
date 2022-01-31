from .secret import get_secret

#################################
# Кэширование
#################################

REDIS_HOST = get_secret(section='REDIS', setting='HOST')
REDIS_PORT = get_secret(section='REDIS', setting='PORT')
REDIS_CACHE_DB = get_secret(section='REDIS', setting='CACHE_DB')


def cache_key_maker(key, key_prefix, version):
    """Убирает приставку (префикс) и версию у redis ключа"""
    return key


def cache_custom_reverse_key(key):
    """Костыль чтоб работал django_redis keys('*') без версионности и префикса"""
    return key


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://{}:{}/{}'.format(
            REDIS_HOST, REDIS_PORT, REDIS_CACHE_DB
        ),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
}
