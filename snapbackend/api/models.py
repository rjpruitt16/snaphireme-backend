from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import logging

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

def deleteCapsuleModels(days=1):
    threshold = timedelta(days=days)
    for capsule in SnapCapsule.objects.all():
        dateToDelete = capsule.dateToPost.replace(tzinfo=None) + threshold
        if datetime.now() > dateToDelete:
            capsule.delete()
            logging.info('Delete capsule: ' + str(capsule))

class SnapCapsule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dateToPost = models.DateTimeField()
    dateToDelete = models.DateTimeField()
    image = models.FileField(upload_to=user_directory_path)
    caption = models.CharField(max_length=20, blank=True)
