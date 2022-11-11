from django import forms

from users.models import CustomUser, Employee, NationList


class EmployeeSignupForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ["first_name", "last_name", "is_teacher", "is_admin"]


# class EmployeeProfileForm(forms.ModelForm):
# 	nation = forms.ModelChoiceField(label="Национальность", widget=forms.Select(), queryset=NationList.objects.all())
#
# 	class Meta:
# 		model = Employee
# 		fields = ("gender",)
