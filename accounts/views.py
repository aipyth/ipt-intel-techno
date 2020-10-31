from django.views.generic import DetailView, View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .models import Competitor
from .forms import CustomUserLoginForm


class CompetitorDetail(DetailView):
    model = Competitor
    template_name = 'accounts/competitor_detail.html'
    context_object_name = 'competitor'


class LoginView(View):
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        form = CustomUserLoginForm()
        context = {
            'form': form
            }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    # user is not yet activated
                    return render(request, 'accounts/competitor_notfound.html')
            else:
                return render(request, 'accounts/competitor_notfound.html')


class LogoutView(View):
    template_name = 'accounts/logout.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, self.template_name)
