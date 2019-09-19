from django.urls import path
from . import views

app_name = "fileupload"

urlpatterns = [
    path('', views.FileUploadView.as_view(), name='upload'),
    path('clear_database/', views.clear_database, name='clear_database'),
]
