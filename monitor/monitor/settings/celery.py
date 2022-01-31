from .secret import get_secret


#################################
# Настройки Celery брокера
#################################
CELERY_BROKER_URL = get_secret(section='CELERY', setting='BROKER_URL')

CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = 'UTC'
CELERY_IGNORE_RESULT = True
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
