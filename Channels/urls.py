"""Channels URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from  django.contrib.auth import views as auth_views
from django.conf.urls import url
from User import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from Echo import views as echo_views

urlpatterns = [
    # path('', include('IQDeviceStatus.urls')),
    path('register/', user_views.register, name ='register_client'),
    path('profile/', user_views.profile, name ='user_profile'),
    path('status/', echo_views.HomeView.as_view() , name='device_status'),
    path('Location/', echo_views.LocationView.as_view() , name= 'location_view'),
    path('', include('main.urls')),
	path('login/', auth_views.LoginView.as_view(template_name ='registration/login.html'), name ='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name ='users/logout.html'), name ='user_logout'),
	path('users/', include('User.urls') , name ='index-base'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
