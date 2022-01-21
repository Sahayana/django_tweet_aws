from django.urls import path
from . import views



urlpatterns = [
    path('signup/', views.sign_up_view, name='signup'),
    path('signin/', views.sign_in_view, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('users/', views.user_list, name='user_list'), 
    path('users/follow/<int:id>/', views.user_follow, name='user_follow'),
    
]