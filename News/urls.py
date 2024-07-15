from django.urls import path
# Импортируем созданные нами представления
from .views import PostList, PostDetail, PostSearch, NewsCreate, NewsUpdate, NewsDelete, ArtsCreate, ArtsDelete, ArtsUpdate, subscriptions

urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('create/', ArtsCreate.as_view(), name='arts_create'),
   path('<int:pk>/edit/', ArtsUpdate.as_view(), name='arts_edit'),
   path('<int:pk>/delete/', ArtsDelete.as_view(), name='arts_delete'),
   path('subscriptions/', subscriptions, name='subscriptions'),
]