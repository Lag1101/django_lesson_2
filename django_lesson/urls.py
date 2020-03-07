from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from . import settings

urlpatterns = [
    path('', include('blog.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
