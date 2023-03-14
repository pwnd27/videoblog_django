from django.shortcuts import render, redirect
from django.views import View
from users.forms import UserRegisterForm


class UserFormView(View):
    form_class = UserRegisterForm
    template_name = 'users/register_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
