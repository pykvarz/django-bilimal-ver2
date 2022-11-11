from django.urls import path, include

from users.views import EmployeeCreateView, EmployeeMainMenu

urlpatterns = [
	path("employee/signup/", EmployeeCreateView.as_view(), name="employee_signup"),
	path("employee/main_menu", EmployeeMainMenu.as_view(), name="employee_main_menu"),
	# path('profile/', ProfileCreateView.as_view(), name='profile_user'),
]