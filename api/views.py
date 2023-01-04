from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from .models import Workspace, Subject, Chapter
from .serializer import WorkspaceSerializer, SubjectSerializer, ChapterSerializer
from .forms import RegisterForm

# Create your views here.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



def RegisterView(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return Response("User created successfully")
        else:
            return Response('An error occurred during registration')
   
    


def default(request):
    return HttpResponse('API is working')
    
class WorkspaceView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        user = request.user
        print(user)
        if pk is not None:
            workspace = user.workspace_set.get(pk=pk)
            seriliazer = WorkspaceSerializer(workspace)
            return Response(seriliazer.data)

        workspaces = user.workspace_set.all()
        seriliazer = WorkspaceSerializer(workspaces, many=True)
        return Response(seriliazer.data)

    def post(self, request):
        data = request.data
        seriliazer = WorkspaceSerializer(data=data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response(seriliazer.data)
        return Response('Error creating workspace!')

    def put(self, request, pk):
        data = request.data
        user = request.user
        workspace = user.workspace_set.get(id=pk)
        seriliazer = WorkspaceSerializer(workspace, data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response(seriliazer.data)
        return Response('Error updating workspace!')

    def delete(self, request, pk):
        user = request.user
        workspace = user.workspace_set.get(id=pk)
        workspace.delete()
        return Response('Workspace deleted!')


class SubjectView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        user = request.user
        if pk is not None:
            subject = user.subject_set.get(id=pk)
            serializer = SubjectSerializer(subject)
            return Response(serializer.data)

        subject = user.subject_set.all()
        serializer = SubjectSerializer(subject, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = SubjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response('Error creating subject!')

    def put(self, request, pk):
        data = request.data
        user = request.user
        subject = user.subject_set.get(id=pk)
        serializer = SubjectSerializer(subject, data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response('Error updating subject!')

    def delete(self, request, pk):
        user = request.user
        subject =  user.subject_set.get(id=pk)
        subject.delete()
        return Response('Subject deleted!')


class ChapterView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        user = request.user
        if pk is not None:
            chapter = user.chapter_set.get(id=pk)
            serializer = ChapterSerializer(chapter)
            return Response(serializer.data)

        chapter = user.chapter_set.all()
        serializer = ChapterSerializer(chapter, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = ChapterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response('Error creating chapter!')

    def put(self, request, pk):
        data = request.data
        user = request.user
        chapter = user.chapter_set.get(id=pk)
        serializer = ChapterSerializer(chapter, data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response('Error updating chapter!')

    def delete(self, request, pk):
        user = request.user
        chapter = user.chapter_set.get(id=pk)
        chapter.delete()
        return Response('Chapter deleted!')


class SubjectOfWorkspaceView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        user = request.user
        if pk is not None:
            subject = user.subject_set.filter(workspace_id=pk)
            serializer = SubjectSerializer(subject, many=True)
            return Response(serializer.data)

        return Response('Invalid Request')


class ChapterOfSubjectView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        user = request.user
        if pk is not None:
            chapter = user.chapter_set.filter(subject_id=pk)
            serializer = ChapterSerializer(chapter, many=True)
            return Response(serializer.data)

        return Response('Invalid Request')
