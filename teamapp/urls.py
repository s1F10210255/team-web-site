from django.contrib import admin
from django.urls import path, include
from teamapp import views as blog_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('welcome.urls')),
]