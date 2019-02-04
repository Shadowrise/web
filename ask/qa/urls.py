from django.conf.urls import url
from qa.views import new, popular, one, ask, signup, login

urlpatterns = [
  url(r'^$', new),
  url(r'^popular/$', popular),
  url(r'^ask/$', ask),
  url(r'^signup/$', signup),
  url(r'^login/$', login),
  url(r'^question/(?P<id>\d+)/$', one),
]
