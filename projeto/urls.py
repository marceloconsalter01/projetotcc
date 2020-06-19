from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('create_clients', views.create_client),
    #path('list_clients', views.list_clients),
    path('admin/', admin.site.urls),
    path('home', views.home_page),
    path('login',views.login_page),
    path('submit',views.submit_login)
    #path('accounts/', include('django.contrib.auth.urls')),
]
