from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'images/user_{0}/{1}'.format(instance.user.id, filename)

def deleteCapsuleModels(days=1):
    threshold = timedelta(days=days)
    for capsule in SnapCapsule.objects.all():
        dateToDelete = capsule.dateToPost.replace(tzinfo=None) + threshold
        if datetime.now() > dateToDelete:
            print("deleted: ")
            capsule.delete()

class SnapCapsule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dateToPost = models.DateTimeField()
    image = models.FileField(upload_to=user_directory_path)
    caption = models.CharField(max_length=20, blank=True)

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.image.storage, self.image.path
        # Delete the model before the file
        super().delete(*args, **kwargs)
        # Delete the file after the model
        print("deleting path")
        storage.delete(path)
