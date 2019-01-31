from django.conf.urls import url
from qa.views import new, popular, one

urlpatterns = [
  url(r'^$', new),
  url(r'^popular/$', popular),
  url(r'^question/(?P<question_id>\d+)$', one),
]
