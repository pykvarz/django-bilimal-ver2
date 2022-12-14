from betterforms.multiform import MultiModelForm
from django import forms

from users.models import CustomUser, Employee, EducationEmployee


class EmployeeSignupForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ["first_name", "last_name", "is_teacher", "is_admin"]


class CurrentEmployeeUpdateCustomUserForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ["first_name", "last_name", ]


class CurrentEmployeeUpdateEmployeeForm(forms.ModelForm):

	class Meta:
		model = Employee
		fields = ["surname", "nation"]


class CustomUserUpdateMultiForm(MultiModelForm):
	form_classes = {
		"user": CurrentEmployeeUpdateCustomUserForm,
		"profile": CurrentEmployeeUpdateEmployeeForm,
	}


class CreateUserEducation(forms.ModelForm):
	class Meta:
		model = EducationEmployee
		fields = ["name", "year_of_admission", "year_of_ending", "speciality", "type_education", ]


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ["first_name", "last_name"]
