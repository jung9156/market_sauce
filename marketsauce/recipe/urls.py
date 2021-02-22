from django.urls import path
from . import views
app_name = 'recipe'

urlpatterns = [
    path('', views.index, name='index'),
    path('write/', views.write, name='write'),
    path('detail/<int:recipe_pk>/', views.detail, name='detail'),
    path('detail_u/<int:recipe_pk>/<int:user_pk>/', views.update, name='update'),
    path('detail_d/<int:recipe_pk>/<int:user_pk>/', views.delete, name='delete'),
    path('detail_r/<int:recipe_pk>/', views.recommend, name='recommend'),
    path('detail_replyup/<int:recipe_pk>/<int:reply_pk>/', views.detail_reply_u, name='reply'),
    path('detail_replydel/<int:recipe_pk>/<int:reply_pk>/', views.detail_reply_d, name='reply_d'),
]   
