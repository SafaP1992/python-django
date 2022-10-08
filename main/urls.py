from django.urls import path
from .views import homeView
from .views import indexView
from .views import blogListView
from .views import blogCreate
from .views import blogDetail
from .views import blogUpdate
from .views import blogDelete

urlpatterns = [
    path('', indexView, name="index-page"),
    path('test/', homeView, name="home-page"),
    path('blog/', blogListView, name="blog-list-page"),
    path('blog/create/', blogCreate, name="blog-create-page"),
    path('blog/<id>/update/', blogUpdate, name="blog-edit-page"),
    path('blog/<id>/', blogDetail, name="blog-single-page"),
    path('blog/<id>/delete/', blogDelete, name="blog-delete-page"),
]