from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView , FormView
from .models import User
from .forms import UserAdminCreationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# @login_required
class UserCreate(CreateView):
	form_class = UserAdminCreationForm
	template_name = 'users/register.html'
	success_url = 'about/'

@login_required
def about(request):
	return render(request , 'users/temp.html')
