from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from tshirt.api import TshirtApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', TshirtApiView.as_view()),
    path('', include('tshirt.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.IMG_URL,
                          document_root=settings.IMG_ROOT)
