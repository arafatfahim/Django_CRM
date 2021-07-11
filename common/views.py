from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
# Create your views here.

class Home(TemplateView):
    template_name = "basics/home.html"

class Test(TemplateView):
    template_name = "basics/test.html"

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "basics/dashboard.html"
    login_url = reverse_lazy('Login')

class SettingsView(LoginRequiredMixin,TemplateView):
    template_name = 'basics/settings.html'
    login_url = reverse_lazy('Login')


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('Home')
    template_name = 'basics/register.html'

from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from user.models import Profile

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'basics/profile.html'

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'basics/profile-update.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return HttpResponseRedirect(reverse_lazy('Profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)