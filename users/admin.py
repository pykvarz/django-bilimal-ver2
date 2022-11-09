from django.contrib import admin

from users.models import CustomUser, Employee


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
	list_display = ("id", CustomUser.get_full_name)
	list_display_links = ("id", CustomUser.get_full_name,)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ("user",)
	list_display_links = ("user",)