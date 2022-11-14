from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
	is_student = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)
	is_employee = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"

	class Meta:
		verbose_name = "Пользователь"
		verbose_name_plural = "Пользователи"


class Student(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)


class Employee(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
	surname = models.CharField(max_length=50, blank=True)
	bio = models.DateField(blank=True, null=True)
	pob = models.CharField(max_length=100)
	GENDER_CHOICES = (
		("ml", "male"),
		("fm", "female"),
	)
	gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default="ml")
	nation = models.CharField(max_length=100)
	citizenship = models.CharField(max_length=100)
	iin = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.user.__str__()

	class Meta:
		verbose_name = "Сотрудник"
		verbose_name_plural = "Сотрудники"


@receiver(post_save, sender=CustomUser)
def create_user_employee(sender, instance, created, **kwargs):
	if created:
		Employee.objects.create(user=instance)


@receiver
def save_user_profile(sender, instance, **kwargs):
	instance.employee.save()


class NationList(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		verbose_name = "Национальность"
		verbose_name_plural = "Национальности"