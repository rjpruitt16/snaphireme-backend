from .base import *

DEBUG = False

ALLOWED_HOSTS = ["rjpruitt22.pythonanywhere.com"]

MEDIA_ROOT = os.path.join(BASE_DIR, "images")
MEDIA_URL = '/snapcapsule/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
