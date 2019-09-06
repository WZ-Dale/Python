"""定义 learning_logs 的 URL 模式"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # 主页.
    url(r'^$', views.index, name='index'),
    
    # Show all topics.
    #url(r'^topics/$', views.topics, name='topics'),
    
    # Detail page for a single topic.
    #url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
