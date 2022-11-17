from users.models import CustomUser


def get_last_id_student():
	try:
		last_id_student = CustomUser.objects.filter(is_employee=1).last().id
		last_id_student = last_id_student + 1
		return last_id_student
	except:
		last_id_student = 1
		return last_id_student


def get_last_id_employee():
	try:
		last_id_teacher = CustomUser.objects.filter(is_employee=1).last().id
		last_id_teacher = last_id_teacher + 1
		return last_id_teacher
	except:
		last_id_teacher = 1
		return last_id_teacher