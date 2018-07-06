import os
os.environ["DJANGO_SETTINGS_MODULE"] = "snapbackend.settings.production"
import django

django.setup()
import snapbackend
from snapbackend.models import deleteCapsuleModels

deleteCapsuleModels()
