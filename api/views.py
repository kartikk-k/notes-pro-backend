from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

from .models import Workspace, Subject, Chapter
from .serializer import WorkspaceSerializer, SubjectSerializer, ChapterSerializer


# Create your views here.
def default(request):
    return HttpResponse('API is working')


class WorkspaceView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            workspace = Workspace.objects.get(pk=pk)
            seriliazer = WorkspaceSerializer(workspace)
            return Response(seriliazer.data)

        workspaces = Workspace.objects.all()
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
        workspace = Workspace.objects.get(id=pk)
        seriliazer = WorkspaceSerializer(workspace, data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response(seriliazer.data)
        return Response('Error updating workspace!')

    def delete(self, request, pk):
        workspace = Workspace.objects.get(id=pk)
        workspace.delete()
        return Response('Workspace deleted!')


class SubjectView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            subject = Subject.objects.get(id=pk)
            serializer = SubjectSerializer(subject)
            return Response(serializer.data)

        subject = Subject.objects.all()
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
        subject = Subject.objects.get(id=pk)
        serializer = SubjectSerializer(subject, data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response('Error updating subject!')

    def delete(self, request, pk):
        subject = Subject.objects.get(id=pk)
        subject.delete()
        return Response('Subject deleted!')


class ChapterView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            chapter = Chapter.objects.get(id=pk)
            serializer = ChapterSerializer(chapter)
            return Response(serializer.data)

        chapter = Chapter.objects.all()
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
        chapter = Chapter.objects.get(id=pk)
        serializer = ChapterSerializer(chapter, data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response('Error updating chapter!')

    def delete(self, request, pk):
        chapter = Chapter.objects.get(id=pk)
        chapter.delete()
        return Response('Chapter deleted!')


class SubjectOfWorkspaceView(APIView):
    def get(self, request, pk):
        if pk is not None:
            subject = Subject.objects.filter(workspace_id=pk)
            serializer = SubjectSerializer(subject, many=True)
            return Response(serializer.data)

        return Response('Invalid Request')


class ChapterOfSubjectView(APIView):
    def get(self, request, pk):
        if pk is not None:
            chapter = Chapter.objects.filter(subject_id=pk)
            serializer = ChapterSerializer(chapter, many=True)
            return Response(serializer.data)

        return Response('Invalid Request')
