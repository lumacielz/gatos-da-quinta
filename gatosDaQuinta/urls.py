from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
import cats.views

urlpatterns = [

                  path('about/', cats.views.AboutView, name="about"),
                  path('cats/', include('cats.urls')),
                  path('donate/', cats.views.DonateView, name="donate"),
                  path('contact/', cats.views.ContactView, name="contact"),
                  path('login/', LoginView.as_view(), name="login"),
                  path('logout/', LogoutView.as_view(next_page='home'), name='logout')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
