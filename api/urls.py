from django.urls import path
from . import views

# create your views here
urlpatterns = [
    path('', views.default, name='api'),

    # get workspaces
    path('workspace/', views.WorkspaceView.as_view(), name='workspaces'),
    path('workspace/<str:pk>/', views.WorkspaceView.as_view(), name='workspace'),
    path('add-workspace/', views.WorkspaceView.as_view(), name='add-workspace'),
    # get subjects of particular workspace
    path('workspace/<str:pk>/subjects/',
         views.SubjectOfWorkspaceView.as_view(), name='subjects-of-workspace'),

    # get subjects
    path('subject/', views.SubjectView.as_view(), name='subjects'),
    path('subject/<str:pk>/', views.SubjectView.as_view(), name='subject'),
    path('add-subject/', views.SubjectView.as_view(), name='add-subject'),
    # get subjects of particular workspace
    path('subject/<str:pk>/chapters/',
         views.ChapterOfSubjectView.as_view(), name='chapters-of-subject'),

    # get subjects
    path('chapter/', views.ChapterView.as_view(), name='chapters'),
    path('chapter/<str:pk>/', views.ChapterView.as_view(), name='chapter'),
    path('add-chapter/', views.ChapterView.as_view(), name='add-chapter'),

]
