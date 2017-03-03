from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from polls.forms import LoginForm
urlpatterns = [
    # Examples:
    # url(r'^$', 'untitled7.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'',include('polls.urls')),
    #url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
    url(r'^login/$', views.login, {'template_name': 'login.html','authentication_form': LoginForm}, name="login") ,
    url(r'^logout/$', views.logout, {'next_page': '/login'}),
]
