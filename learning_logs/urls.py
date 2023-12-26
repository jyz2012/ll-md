from django.urls import path, re_path
from . import views

app_name='learning_logs'

urlpatterns=[
	#home
	path('',views.index,name='index'),
    # path('pic/',views.pic,name='pic'),
	#topics
	path('topics/',views.topics,name='topics'),
	#xiangxi
	path('topics/<int:topic_id>/',views.topic,name='topic'),
	#addnewzt
	path('new_topic/',views.new_topic,name='new_topic'),
	#newentry
	path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),
	#editentry
	path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),
    
	path('my_topics/', views.my_topics, name='my_topics'),
	# 用于删除自有条目的页面
	re_path('delete_entry/(?P<entry_id>\d+)/', views.delete_entry, name='delete_entry'),

	# 用于删除自有主题的页面
	re_path('delete_topic/(?P<topic_id>\d+)/', views.delete_topic, name='delete_topic'),
]