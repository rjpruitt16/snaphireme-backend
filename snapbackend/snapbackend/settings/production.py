from .base import *

DEBUG = False

ALLOWED_HOSTS = ["rjpruitt22.pythonanywhere.com"]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

MEDIA_ROOT = os.path.join(BASE_DIR, "images")
MEDIA_URL = '/snapcapsule/images/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
