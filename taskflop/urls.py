from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin

from django.views.generic import TemplateView


urlpatterns = patterns(
    '',

    # Django administration
    url(r'^admin/', include(admin.site.urls)),

    # Placeholder page to display until the app is ready for public use
    url(
        r'^$',
        TemplateView.as_view(template_name='placeholder.html'),
        name='placeholder'
    ),
)

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
