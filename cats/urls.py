from django.urls import path

from .views import HomePageView,CreateView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('new/', CreateView, name="create")
]
