from django.conf.urls import url, include
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from thoughts.views import IndexView, UserCreateView, CategoryCreateView, ProfileUpdateView, \
                           ProfileCreateView, CategoryListView, CategoryDetailView, BlogCreateView, \
                           BlogDetailView, CategoryUpdateView, BlogTextUpdateView, BlogTitleUpdateView, \
                           ReplyCreateView, ReplyUpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^', include('django.contrib.auth.urls'), name='login'),
    url(r'^new_user/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^category/create/$', CategoryCreateView.as_view(), name='category_create_view'),
    url(r'^profile/create/$', ProfileCreateView.as_view(), name='profile_create_view'),
    url(r'^profile/update/(?P<random_url>[-\w]+)/(?P<pk>\d+)/$', ProfileUpdateView.as_view(), name='profile_update_view'),
    url(r'^category/$', CategoryListView.as_view(), name='category_list_view'),
    url(r'^category/(?P<random_url>[-\w]+)/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name='category_detail_view'),
    url(r'^category/(?P<random_url>[-\w]+)/(?P<pk>\d+)/new_entry/$', BlogCreateView.as_view(), name='blog_create_view'),
    url(r'^category/(?P<random_url>[-\w]+)/(?P<pk>\d+)/update/$', CategoryUpdateView.as_view(), name='category_update_view'),
    url(r'^post/(?P<random_url>[-\w]+)/(?P<pk>\d+)/$', BlogDetailView.as_view(), name='blog_detail_view'),
    url(r'^post/(?P<random_url>[-\w]+)/(?P<pk>\d+)/update_text/$', BlogTextUpdateView.as_view(), name='blog_text_update_view'),
    url(r'^post/(?P<random_url>[-\w]+)/(?P<pk>\d+)/update_title/$', BlogTitleUpdateView.as_view(), name='blog_title_update_view'),
    url(r'^post/(?P<random_url>[-\w]+)/(?P<pk>\d+)/reply/$', ReplyCreateView.as_view(), name='reply_create_view'),
    url(r'reply/(?P<pk>\d+)/update/$', ReplyUpdateView.as_view(), name='reply_update_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
