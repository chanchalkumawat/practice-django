from django.urls import path
from music import views

urlpatterns = [
    # ex: /music/
    path('', views.index, name='index'),
    # ex: /music/5/
    path('<int:album_id>/', views.detail, name='detail')
]