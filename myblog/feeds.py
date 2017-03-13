from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from myblog.models import Post
from myblog.views import detail_view

class LatestPostsFeed(Feed):
	title = "Myblog posts"
	link = "/latest/feed"
	description = "Latest posts"

	def items(self):
		return Post.objects.order_by('-published_date')[:5]

	def item_title(self, item):
		return item.title

	def item_text(self, item):
		return item.text

# item_link is only needed if NewsItem has no get_absolute_url method.
	def item_link(self, item):
		#return reverse('text', kwargs={'post_id':item.pk})
		return reverse('blog_detail', kwargs={'post_id':item.pk})
