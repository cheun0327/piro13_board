from django.urls import path
from . import views

# 프로젝트 파일(config) > urls.py에 설정한 board path의 namespace와 같아야 한다
app_name = "board"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("detail/<int:pk>/", views.post_detail, name="post_detail"),
    path("create/", views.post_create, name="post_create"),
    path("delete/<int:pk>", views.post_delete, name="post_delete"),
    path("update/<int:pk>", views.post_update, name="post_update"),
]
