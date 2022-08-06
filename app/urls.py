from django.urls import path
from . import views


urlpatterns = [
    path('useraccount/<int:pk>/', views.user_profile, name='useraccount'),
    path('updateaccount/', views.user_profile_update, name='updateaccount'),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    path('', views.house_list, name='houses'),
    path('house/<int:pk>/', views.house_detail, name='house'),

    path('houseupdate/<int:pk>/', views.house_edit, name='houseupdate'),
    path('housecreate/', views.house_create, name='housecreate'),
    path('housedelete/<int:pk>/', views.house_delete, name='housedelete'),
]
