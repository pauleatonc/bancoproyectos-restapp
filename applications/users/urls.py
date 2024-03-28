from django.urls import path, include, re_path

from .views import Login, Logout, keycloak_code_exchange_view

app_name = 'users_app'

urlpatterns = [

    re_path('', include('applications.users.api.v1.routers')),
    path(
        'login/',
        Login.as_view(),
        name='login',
    ),
    path(
        'logout/',
        Logout.as_view(),
        name='logout',
    ),
     path(
         'callback/', keycloak_code_exchange_view, name='callback'
    ),
    
]