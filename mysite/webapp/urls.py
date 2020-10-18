from django.urls import path
from .import views

urlpatterns = [
    path('', views.publications, name='home'),
    path('authors', views.authors, name='authors'),
    path('CreatePublication', views.create_pub, name='create1'),
    path('CreateAuthor', views.create_auth, name='create2'),
]
