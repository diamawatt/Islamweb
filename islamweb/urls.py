from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('infos.urls')),
    path('zone-secrete-diamathereal/', admin.site.urls),
    path('prieres/', include('prayers.urls')),
    path('grappelli/', include('grappelli.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
