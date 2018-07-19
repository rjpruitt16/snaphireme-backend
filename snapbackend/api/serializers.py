from api.models import SnapCapsule
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from rest_framework import serializers

class SnapCapsuleSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = SnapCapsule
        fields = ('user', 'dateToPost', 'dateToDelete', 'image', 'caption',
                  'url', 'username',
                  )

    def validate_dateToPost(self, value):
        present = datetime.now()
        present = present - timedelta(minutes=5)
        value = value.replace(tzinfo=None)
        if value < present:
            raise serializers.ValidationError("%s date must greater than present: %s"
                                              % (str(value), str(present)))
        return value

    def get_username(self, object):
        return object.user.username


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snapcapsules = SnapCapsuleSerializer(
        many=True,
        read_only=True,
        allow_null=True,
    )

    class Meta:
        model = User
        fields = ('snapcapsules', 'url', 'username', 'email', 'password')
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        assert (validated_data), "No data recieved."
        for capsule in validated_data.get("snapcapsules", []):
            snapcapsulea = instance.snapcapsules
            snapcapsule = SnapCapsule.object.create(user=instance.username,
                                                    **capsule)
            snapcapsule.save()
            snapcapsules.append(snapcapsule)
            instance.snapcapsules = snapcapsule
            instance.save()

        return instance
