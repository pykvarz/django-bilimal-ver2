from django.urls import path

from users.views import EmployeeCreateView, EmployeeMainMenu, EmployeeListView, EmployeeDetailView, CurrentEmployeeDetailView, MyProfileUpdateView

urlpatterns = [
	path("employee/signup/", EmployeeCreateView.as_view(), name="employee_signup"),
	path("employee/main_menu", EmployeeMainMenu.as_view(), name="employee_main_menu"),
	path("employee/list", EmployeeListView.as_view(), name="employee_list"),
	path("employee/<int:pk>", EmployeeDetailView.as_view(), name="employee_profile"),
	path("my_profile/", CurrentEmployeeDetailView.as_view(), name="current_employee_detail"),
	path("my_profile/update/", MyProfileUpdateView.as_view(), name="my_profile_update"),
	# path('profile/', ProfileCreateView.as_view(), name='profile_user'),
]