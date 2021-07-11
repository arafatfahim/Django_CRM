"""Django_CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.urls.conf import include
from common.views import SignUpView, Home, DashboardView,Test, ProfileUpdateView, ProfileView, SettingsView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from emailer import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='Home'),
    #path('test/', Test.as_view(), name='Test'),
    path('email/', TemplateView.as_view(template_name="basics/email.html"), name='Email'),
    path('send-form-email/', views.SendFormEmail.as_view(), name='send_email'),
    path('signup/', SignUpView.as_view(), name='SignUp'),
    path('login/', auth_views.LoginView.as_view(template_name="basics/login.html"), name='Login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='Home'), name='Logout'),
    path('settings/', auth_views.PasswordChangeView.as_view(template_name="basics/settings.html", success_url='Dashboard'), name='Settings'),
    path('dashboard/', DashboardView.as_view(), name='Dashboard'),
    path('settings/', SettingsView.as_view(), name='Settings'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='basics/password-reset/password_reset.html',
             subject_template_name='basics/password-reset/password_reset_subject.txt',
             email_template_name='basics/password-reset/password_reset_email.html',
             # success_url='/Login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='basics/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='basics/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='basics/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('profile-update/', ProfileUpdateView.as_view(), name='Profile-update'),
    path('profile/', ProfileView.as_view(), name='Profile'),
    path('oauth/', include('social_django.urls', namespace='Social')),
    path('api/', include('user.api.urls'))

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    