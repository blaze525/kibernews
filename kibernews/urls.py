from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings
from . import views


main_app_patterns = [
    path('', include('main.urls')),
]

main_app_patterns = i18n_patterns(
    *main_app_patterns,
    prefix_default_language=False,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    *main_app_patterns,
    path('set_language/<str:language>', views.set_language, name='set-language')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)