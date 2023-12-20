
from django.urls import path
from .views import home, add_album, add_musician, edit_album, edit_musician, delete_album
urlpatterns = [
    path('', home, name="home"),
    path('add_musician/', add_musician, name="add_musician"),
    path('add_album/', add_album, name="add_album"),
    path('edit_album/<int:id>/', edit_album, name="edit_album"),
    path('edit_musician/<int:id>/', edit_musician, name="edit_musician"),
    path('delete_album/<int:id>/', delete_album, name="delete_album"),
]
