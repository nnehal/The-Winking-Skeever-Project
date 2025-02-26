"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from employee import views as employee_views
from post import views as post_views
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', post_views.index, name='page-index'),
    path('post/', post_views.post_schedule, name='"page-postschedule"'),
    path('profile/', employee_views.profile, name='"page-profile"'),
    path('schedule/', include('schedule.urls')),
    path('register/', employee_views.register, name='page-register'),
    path('login/', auth_views.LoginView.as_view(template_name='employee/login.html'), name='page-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='employee/logout.html'), name='page-logout'),
    path('admin/', admin.site.urls)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
