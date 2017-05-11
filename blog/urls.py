from django.conf.urls import url, include
from django.contrib import admin

from thoughts.views import IndexView, UserCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^', include('django.contrib.auth.urls'), name='login'),
    url(r'^new_user/$', UserCreateView.as_view(), name='user_create_view'),
]
