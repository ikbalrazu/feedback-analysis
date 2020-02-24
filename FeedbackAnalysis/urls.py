
# admin username: superuser password: user123

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from UserPage import views as users_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',users_view.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('',include('HomePage.urls')),
]
