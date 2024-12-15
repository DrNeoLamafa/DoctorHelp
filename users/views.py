from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from users.forms import *
from django.contrib.messages.views import SuccessMessageMixin




class UserLoginView(SuccessMessageMixin, LoginView):
    """
    Авторизация на сайте
    """
    form_class = LoginForm
    template_name = 'login.html'
    next_page = '/'
    success_message = 'Добро пожаловать на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация на сайте'
        return context

def SignUp(request):
	if request.user.is_authenticated:
		return redirect('/')
	else: 
		if request.method == 'POST':
			form = RegistrationForm(request.POST)
			if form.is_valid():
				email = request.POST.get('email')
				password1 = request.POST.get('password1')
				
				user = CustomUser.objects.create_user(
					
					username=email,
					email=email
				)
				user.set_password(password1)
				user.save()
				auth = authenticate(username=email, password=password1)
				
				login(request, auth)
				messages.success(request, 'Регистрация успешна')
				return redirect('/')
			else:
				return render(request, 'signup.html', {'form':form}) 
		
		return render(request, 'signup.html', {'form':RegistrationForm()})