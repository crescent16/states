from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.utils.html import escape

from app import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #edit views URL


    url(r'^edit_state/(?P<pk>\d+)/$', 'app.views.edit_state', name='edit_state'),

    url(r'^delete_city/(?P<pk>\d+)/$', 'app.views.delete_city'),

    url(r'^city_list/$', 'app.views.city_list'),

    #edit views
    url(r'^edit_city/(?P<pk>\d+)/$', 'app.views.edit_city', name='edit_city'),

    #create views
    url(r'^create_city/', 'app.views.create_city'),
    url(r'^city_search_post/', 'app.views.city_search'),



    url(r'^city_search/', 'app.views.city_search'),

    url(r'^state_list/', 'app.views.state_list'),
    url(r'^state_detail/(?P<pk>\d+)', 'app.views.state_detail'),
    
    url(r'^list/', 'app.views.list'),

    url(r'^detail/(?P<pk>\d+)', 'app.views.detail'),

    url(r'^template_view2/', 'app.views.template_view2'),

    url(r'^template_view/', 'app.views.template_view'),

    url(r'^class_based_view/', views.GetPost.as_view()),

    url(r'^admin/', include(admin.site.urls)), 

    url(r'^form_view/', 'app.views.form_view'),

    url(r'^get_post/', 'app.views.get_post'),

    url(r'^first_view/$', 'app.views.first_view'),
    url(r'^second_view/$', 'app.views.second_view'),
    url(r'^third_view/$', 'app.views.third_view'),
    
    # url(r'^state_list/(?P<letter>\w+)/(?P<sort>\w+)/','app.views.state_list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)