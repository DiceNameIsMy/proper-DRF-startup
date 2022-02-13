from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

# fmt: off

urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/", include((
        [
            path("accounts/", include("accounts.api.v1.urls")),
        ],
        "v1",
    ))),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
