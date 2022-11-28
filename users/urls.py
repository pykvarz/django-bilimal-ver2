from django.urls import path

from users.models import Employee
from users.views import EmployeeCreateView, EmployeeMainMenu, EmployeeListView, EmployeeDetailView, CurrentEmployeeDetailView, MyProfileUpdateView, \
	UserEducationListView, CreateUserEducationView, ProfileUpdateView

urlpatterns = [
	path("employee/signup/", EmployeeCreateView.as_view(), name="employee_signup"),
	path("employee/main_menu", EmployeeMainMenu.as_view(), name="employee_main_menu"),
	path("employee/list", EmployeeListView.as_view(), name="employee_list"),
	path("employee/<int:pk>/profile/", EmployeeDetailView.as_view(), name="employee_profile"),
	path("employee/<int:pk>/update/", ProfileUpdateView.as_view(), name="update_profile"),
	# path("employee/<int:pk>/profile/update/", EmployeeProfileUpdateView.as_view(), name="employee_profile_update"),
	# path("employee/educations/<int:pk>", EmployeeEducationListView.as_view(), name="employee_education_list"),
	# path("employee/educations/<int:pk>/create/", EmployeeEducationCreateView.as_view(), name="employee_education_create"),

	path("my_profile/", CurrentEmployeeDetailView.as_view(), name="current_employee_detail"),
	path("my_profile/update/", MyProfileUpdateView.as_view(), name="my_profile_update"),
	path("my_profile/educations/<int:pk>/", UserEducationListView.as_view(), name="user_education_list"),
	path("my_profile/educations/create/<int:pk>", CreateUserEducationView.as_view(), name="user_education_create"),
]