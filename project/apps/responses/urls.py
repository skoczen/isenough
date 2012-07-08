from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'responses.views.begin', name='begin'),
    url(r'^respond$', 'responses.views.entry', name='respond'),
    url(r'^saved$', 'responses.views.saved', name='saved'),
    url(r'^display-all$', 'responses.views.display_all', name='display_all'),
    url(r'^display-one$', 'responses.views.display_one', name='display_one'),
    

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
