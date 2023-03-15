from django.views.generic.edit import FormView
from users.forms import UserRegisterForm
from django.urls import reverse_lazy


class UserFormView(FormView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

