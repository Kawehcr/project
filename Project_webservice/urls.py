from django.urls import path
from project.views import ProjectCreateViewSet
from project.views import ProjectRetrieveUpdateDeleteViewSet
from project.views import ProjectListViewSet
from project.views import RequestTestAPI

urlpatterns = [
    path("api/v1/projects/create", ProjectCreateViewSet.as_view(), name="project_create"),
    
    path("api/v1/projects/<int:pk>/retrieve", ProjectRetrieveUpdateDeleteViewSet.as_view(), name="project_retrieve"),

    path("api/v1/projects/<int:pk>/update", ProjectRetrieveUpdateDeleteViewSet.as_view(), name="project_update"),

    path("api/v1/projects/<int:pk>/delete", ProjectRetrieveUpdateDeleteViewSet.as_view(), name="project_delete"),

    path("api/v1/projects/list", ProjectListViewSet.as_view(), name="project_list"),

    path("api/v1/request/", RequestTestAPI.as_view(), name="project_test"),
]
