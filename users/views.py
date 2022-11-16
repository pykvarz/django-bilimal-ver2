from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView

from users.forms.user_form import EmployeeSignupForm, CustomUserUpdateMultiForm
from users.helpers.last_id import get_last_id_employee
from users.models import CustomUser


class EmployeeCreateView(CreateView):
	model = CustomUser
	template_name = "registration/employee_register.html"
	form_class = EmployeeSignupForm

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'teacher'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		new_user = CustomUser.objects.create(username=f"s130t{get_last_id_employee()}", password=make_password("123"), is_employee=True)
		new_user.save()
		login(self.request, new_user)
		return redirect("employee_main_menu")


class EmployeeListView(ListView):
	model = CustomUser
	template_name = "employee_list.html"

	def get_context_data(self, **kwargs):
		context = super(EmployeeListView, self).get_context_data(**kwargs)
		context["teachers"] = CustomUser.objects.filter(is_teacher=True, is_employee=True, is_active=True)
		return context


class EmployeeDetailView(DetailView):
	model = CustomUser
	template_name = "employee_profile.html"
	context_object_name = "user_employee"


class CurrentEmployeeDetailView(DetailView):
	model = CustomUser
	template_name = "current_employee_profile.html"
	context_object_name = "current_employee"

	def get_object(self, *args, **kwargs):
		return get_object_or_404(CustomUser, id=self.request.user.id)


class MyProfileUpdateView(UpdateView):
	model = CustomUser
	template_name = "current_employee_profile_update.html"
	form_class = CustomUserUpdateMultiForm
	success_url = reverse_lazy("current_employee_detail")

	def get_object(self, *args, **kwargs):
		return get_object_or_404(CustomUser, id=self.request.user.id)

	def get_form_kwargs(self):
		kwargs = super(MyProfileUpdateView, self).get_form_kwargs()
		kwargs.update(instance={
			'user': self.object,
			'profile': self.object.employee,
		})
		return kwargs


class EmployeeMainMenu(TemplateView):
	template_name = "employee_main_menu.html"
