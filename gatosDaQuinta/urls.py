from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

import cats.views
from cats.views import Login

urlpatterns = [
                  path('cats/', include('cats.urls')),
                  path('about/', cats.views.AboutView, name="about"),
                  path('contact/', cats.views.ContactView),
                  path('admin/', admin.site.urls),
                  path('accounts/', include('django.contrib.auth.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
