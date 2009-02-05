from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'testsite.mainapp.views.index'), # Main page, links
    (r'^register/$','testsite.mainapp.views.register'), # Page with register form
    (r'^login/$','testsite.mainapp.views.login'), # Page with login form
    (r'^forgot/$','testsite.mainapp.views.forgot'), # Page with retrieve login form
    (r'^forgot/done/$','testsite.mainapp.views.forgot_message'),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'template_name':'resetpassword/form_reset.tpl'}),
    (r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', {'template_name':'resetpassword/reset_message.tpl'})
)
