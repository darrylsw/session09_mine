from django.conf.urls import url
from myblog.views import stub_view
from myblog.views import list_view
from myblog.views import detail_view
from myblog.feeds import LatestPostsFeed

urlpatterns = [
    url(r'^$',
        list_view,
        name="blog_index"),

    url(r'^posts/(?P<post_id>\d+)/$',
        detail_view,
        name="blog_detail"),

	url(r'^latest/feed/$', LatestPostsFeed()),
]

