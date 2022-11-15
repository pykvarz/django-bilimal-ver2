from betterforms.multiform import MultiModelForm
from django import forms
from django.http import HttpResponseRedirect

from users.models import CustomUser, Employee, NationList


class EmployeeSignupForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ["first_name", "last_name", "is_teacher", "is_admin"]


class CurrentEmployeeUpdateCustomUserForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ["first_name", "last_name", ]


class CurrentEmployeeUpdateEmployeeForm(forms.ModelForm):
	nation = forms.ModelChoiceField(label="Национальность", widget=forms.Select(), queryset=NationList.objects.all())

	class Meta:
		model = Employee
		fields = ["surname"]


class CustomUserUpdateMultiForm(MultiModelForm):
	form_classes = {
		"user": CurrentEmployeeUpdateCustomUserForm,
		"profile": CurrentEmployeeUpdateEmployeeForm,
	}
