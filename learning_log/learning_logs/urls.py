# -*- coding: UTF-8 -*-
"""
@Project ：web_api 
@File    ：urls.py.py
@Author  ：ChengXiaozhao
@Date    ：2021/2/15 下午8:54 
@Desc    ：定义learning_log的URL模式
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),   # 主页
    url(r'^topics/$', views.topics, name='topics'),   # 主题
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),   # 特定主题的详情
    url(r'^new_topic/$', views.new_topic, name='new_topic'),     # 添加新的主题
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),     # 添加新条目
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry')    # 编辑新条目
]
