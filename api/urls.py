from django.urls import path
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from . import views

# create your views here
urlpatterns = [
    path('', views.default, name='api'),
    path('register/', views.RegisterView, name='register-user'),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # get workspaces
    path('workspace/', views.WorkspaceView.as_view(), name='workspaces'),
    path('workspace/<str:pk>/', views.WorkspaceView.as_view(), name='workspace'),
    # get subjects of particular workspace
    path('workspace/<str:pk>/subjects/',
         views.SubjectOfWorkspaceView.as_view(), name='subjects-of-workspace'),

    # get subjects
    path('subject/', views.SubjectView.as_view(), name='subjects'),
    path('subject/<str:pk>/', views.SubjectView.as_view(), name='subject'),
    # get subjects of particular workspace
    path('subject/<str:pk>/chapters/',
         views.ChapterOfSubjectView.as_view(), name='chapters-of-subject'),

    # get subjects
    path('chapter/', views.ChapterView.as_view(), name='chapters'),
    path('chapter/<str:pk>/', views.ChapterView.as_view(), name='chapter'),
]
