from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
import cats.views


urlpatterns = [
                  path('cats/', include('cats.urls')),
                  path('about/', cats.views.AboutView, name="about"),
                  path('contact/', cats.views.ContactView),
                  path('login/', LoginView.as_view(), name="login"),
                  path('logout/', LogoutView.as_view(next_page='login'), name='logout')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
