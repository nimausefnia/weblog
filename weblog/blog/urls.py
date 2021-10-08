from django.urls import path
from . import views

app_name='blog'
urlpatterns=[
      path('',views.all_article, name='all_article'),
      path('<int:id>/<slug:slug>/', views.article, name='article_detail'),

]