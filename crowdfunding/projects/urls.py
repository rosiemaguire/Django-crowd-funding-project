from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('pledges/<int:pk>/', views.PledgeDetail.as_view()),
    path('api/pledges/<int:pk>/', views.PledgeDeleteView.as_view(), name='pledge-delete'),
    path('api/projects/<int:pk>/', views.ProjectDeleteView.as_view(), name='project-delete'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
