from django.conf.urls import url, include
from django.contrib import admin

from thoughts.views import IndexView, UserCreateView, CategoryCreateView, ProfileUpdateView, \
                           ProfileCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^', include('django.contrib.auth.urls'), name='login'),
    url(r'^new_user/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^category/create/$', CategoryCreateView.as_view(), name='category_create_view'),
    url(r'^profile/create/$', ProfileCreateView.as_view(), name='profile_create_view'),
    url(r'^profile/update/(?P<user>[-\w]+)/(?P<pk>\d+)/$', ProfileUpdateView.as_view(), name='profile_update_view'),
]
