
from django.conf.urls import url
# importing views
from . import views

app_name = 'music'

urlpatterns = [
    #Default homepage (index)
    url(r'^$', views.index, name='index'),
    #/music/<album id > /
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    #/music/<album id>/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite')
]
