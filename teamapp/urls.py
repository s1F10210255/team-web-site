from django import urls
from django.contrib import admin
from django.urls import path, include
from teamapp import views as blog_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('welcome.urls')),
    path('about/',include('about_us.urls')),
    path('contact/',include('contact_us.urls')),
]