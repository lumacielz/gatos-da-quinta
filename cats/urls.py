from django.urls import path

from .views import HomePageView, CreateView, EditView, DeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('new', CreateView, name="create"),
    path('edit/<int:id>', EditView, name="edit"),
    path('<int:id>', DeleteView, name="delete")
]
