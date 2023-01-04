from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from . import views
from .models import User

# create your serializers here
# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password']

#         def create(self, validated_data):
#             # user.set_password(validated_data['password'])
#             user.set_password = make_password(user.password)
#             user = User.objects.create(**validated_data)
#             password = validated_data.pop('password', None)
#             instance = self.Meta.model(**validated_data)
#             extra_kwargs = {
#                 'password': {'write_only': True}
#             }
#             if password is not None:
#                 instance.set_password(password)
#             instance.save()
#             return instance
    

class WorkspaceSerializer(ModelSerializer):
    class Meta:
        model = views.Workspace
        fields = '__all__'


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = views.Subject
        fields = '__all__'


class ChapterSerializer(ModelSerializer):
    class Meta:
        model = views.Chapter
        fields = '__all__'
