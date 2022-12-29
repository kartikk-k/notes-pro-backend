from rest_framework.serializers import ModelSerializer
from . import views

# create your serializers here


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
