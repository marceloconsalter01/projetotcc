from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page),
    path('home', views.home_page),
    path('create_clients', views.create_clients),  # --->  Rota de Rederizar pagina
    path('insert_client', views.insert_client),   #---> Rota da função
    path('list_clients', views.list_page),
    path('admin/', admin.site.urls),
    path('login', views.login_page),
    path('submit', views.submit_login),
    path('redirect', views.redirect_page),
    path('ConsultClient',views.ConsultClient),
    path('edit_client',views.edit_page),
    path('EditClient',views.EditClient),
    path('DeleteMongo',views.Deletedb)
    # path('accounts/', include('django.contrib.auth.urls')),
]
