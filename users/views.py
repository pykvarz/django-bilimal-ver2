from tkinter import Menu

from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from pyexpat import model

from users.forms.user_form import EmployeeSignupForm
from users.helpers.last_id import get_last_id_employee
from users.models import Employee, CustomUser


# class ProfileCreateView(CreateView):
# 	model = Employee
# 	form = EmployeeProfileForm
# 	template_name = "templates/employee_profile.html"


class EmployeeCreateView(CreateView):
	model = CustomUser
	template_name = "registration/employee_register.html"
	form_class = EmployeeSignupForm

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'teacher'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		new_user = CustomUser.objects.create(username=f"s130t{get_last_id_employee()}", password=make_password("123"))
		new_user.save()
		login(self.request, new_user)
		return redirect("employee_main_menu")


class EmployeeMainMenu(TemplateView):
	template_name = "employee_main_menu.html"


