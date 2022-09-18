from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='houses'),
    path('house/<str:pk>/', views.house_detail, name='house'),
    path('edit/<str:pk>/', views.house_update, name='edit'),
    path('delete/<str:pk>/', views.house_delete, name='delete'),
    path('create/', views.house_create, name='create'),

    path('profile/<str:pk>/', views.agent_profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile-update/', views.profile_update, name='profile-update'),
    path('signup/', views.sign_up, name='signup'),
]
