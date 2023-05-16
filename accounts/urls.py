from django.urls import path
from . import views
from .views import ProfileUpdateView
app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('edit/', views.edit, name='edit'),
    path('<int:user_pk>/follow/', views.follow, name='follow',),
    path('<username>/', views.profile, name='profile'),
    path('profile/update/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update'),
]
