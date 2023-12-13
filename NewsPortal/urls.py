from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path("accounts/", include("allauth.urls")),
   path('pages/', include('django.contrib.flatpages.urls')),
   path('news/', include('News.urls')),
   path('articles/', include('News.urls')),
]