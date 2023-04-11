from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import View


class LoginPageView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard:list')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,
                            password=password, )
        if user is not None:
            login(request, user)
            return redirect('auth:login')
        message = 'Entered bad credentials!'
        return render(request, self.template_name, context={'message': message})
