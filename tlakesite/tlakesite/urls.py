from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
import tlakesite.settings

urlpatterns = patterns(
    '',

    # Examples:
    # url(r'^$', 'tlakesite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('home.urls')),
    url(r'^projects/', include('projects.urls')),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(tlakesite.settings.MEDIA_URL, document_root=tlakesite.settings.MEDIA_ROOT)
