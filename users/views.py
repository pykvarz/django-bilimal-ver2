from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView

from users.forms.user_form import EmployeeSignupForm, CustomUserUpdateMultiForm, CreateUserEducation, ProfileUpdateForm
from users.helpers.last_id import get_last_id_employee
from users.models import CustomUser, EducationEmployee


class EmployeeCreateView(CreateView):
	model = CustomUser
	template_name = "registration/employee_register.html"
	form_class = EmployeeSignupForm

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.username = f"s130t{get_last_id_employee()}"
		instance.password = make_password("123")
		instance.is_employee = True
		instance.save()
		login(self.request, instance)
		return redirect("employee_main_menu")


class EmployeeListView(LoginRequiredMixin, ListView):
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


class CreateUserEducationView(LoginRequiredMixin, CreateView):
	model = EducationEmployee
	template_name = "create_user_education.html"
	form_class = CreateUserEducation
	success_url = reverse_lazy("employee_main_menu")

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user_id = self.kwargs['user_id']
		instance.save()
		return super(CreateUserEducationView, self).form_valid(form)


# def get_form_kwargs(self):
# 	kwargs = super().get_form_kwargs()
# 	return kwargs


class UserEducationListView(ListView):
	model = EducationEmployee
	template_name = "employee_education_list.html"
	context_object_name = "educations"

	def get_context_data(self, **kwargs):
		context = super(UserEducationListView, self).get_context_data(**kwargs)
		context["educations"] = EducationEmployee.objects.filter(user_id=self.kwargs['pk'])
		# context["educations"] = EducationEmployee.objects.filter(user_id=self.kwargs.get(self.pk_url_kwarg, None))
		context["user"] = CustomUser.objects.get(pk=self.kwargs['pk'])
		return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
	model = CustomUser
	template_name = "profile_update.html"
	form_class = CustomUserUpdateMultiForm
	success_url = reverse_lazy("employee_main_menu")

	def get_form_kwargs(self):
		kwargs = super(ProfileUpdateView, self).get_form_kwargs()
		print(kwargs["instance"].username)
		print(self.request.user.username)
		if self.request.user.is_admin:
			kwargs.update(instance={
				'user': self.object,
				'profile': self.object.employee,
			})
			return kwargs
		if self.request.user.username != kwargs["instance"].username:
			return self.handle_no_permission()
		else:
			kwargs.update(instance={
				'user': self.object,
				'profile': self.object.employee,
			})
			return kwargs


class EmployeeMainMenu(TemplateView):
	template_name = "employee_main_menu.html"
