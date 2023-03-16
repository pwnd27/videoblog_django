from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from users.forms import UserRegisterForm, UserAuthenticationForm
from django.urls import reverse_lazy


class UserRegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserLoginView(LoginView):
    form_class = UserAuthenticationForm
    template_name = 'users/login.html'
