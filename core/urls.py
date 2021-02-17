from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from . import settings
from django.contrib import admin
from django.urls import include, path

handler400 = "ajversh.views.error_400"

handler403 = "ajversh.views.error_403"

handler404 = "ajversh.views.error_404"

handler500 = "ajversh.views.error_500"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(("ajversh.urls", "ajversh"))),
    path("", include('allauth.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
