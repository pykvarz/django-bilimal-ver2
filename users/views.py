from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView

from users.forms.user_form import EmployeeSignupForm, CustomUserUpdateMultiForm, CreateUserEducation
from users.helpers.last_id import get_last_id_employee
from users.models import CustomUser, EducationEmployee


class EmployeeCreateView(CreateView):
	model = CustomUser
	template_name = "registration/employee_register.html"
	form_class = EmployeeSignupForm

	def form_valid(self, form):
		instance = form.save(commit=False)
		# new_user = CustomUser.objects.create(username=f"s130t{get_last_id_employee()}", password=make_password("123"), is_employee=True)
		# new_user.save()
		instance.username = f"s130t{get_last_id_employee()}"
		instance.password = make_password("123")
		instance.is_employee = True
		instance.save()
		login(self.request, instance)
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


class CreateUserEducationView(CreateView):
	model = EducationEmployee
	template_name = "create_user_education.html"
	form_class = CreateUserEducation

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user_id = self.request.user.id
		instance.save()
		return redirect('user_education_list')


class UserEducationListView(ListView):
	model = EducationEmployee
	template_name = "employee_education_list.html"

	def get_context_data(self, **kwargs):
		context = super(UserEducationListView, self).get_context_data(**kwargs)
		context["educations"] = EducationEmployee.objects.filter(user_id=self.request.user.id)
		return context


class EmployeeMainMenu(TemplateView):
	template_name = "employee_main_menu.html"
