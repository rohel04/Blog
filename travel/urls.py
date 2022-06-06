from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
   
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('connect',views.connect,name='connect'),
    path('detail/<int:post_id>',views.detail,name='detail'),
    path('edit/<int:post_id>',views.edit,name='edit'),
    path('delete/<int:post_id>',views.delete,name='delete'),
    path('tags/<int:cat_id>',views.tags,name='tags'), 
    path('blogs',views.blogs,name='blogs'),
    path('add_blog',views.add_blog,name='add_blog'),
    path('send_blog',views.receive_blog,name='send_blog'),
    path('myblogs',views.myblogs,name='myblogs'),

    path('detail/add_comment',views.add_comment,name='add_comment'),
    path('detail/delete_comment/<int:cmt_id>',views.delete_comment,name='delete_comment')
]