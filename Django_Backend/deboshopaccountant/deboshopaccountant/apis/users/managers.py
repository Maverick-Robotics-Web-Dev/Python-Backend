from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserEmployeeManager(BaseUserManager, models.Manager):

    def _create_user(self, user_employee_user_name, user_employee_password, is_staff, is_superuser, is_active, **extra_fields):
        user_Employee_model = self.model(
            user_employee_user_name=user_employee_user_name,
            user_employee_password=user_employee_password,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user_Employee_model.set_password(user_employee_password)
        user_Employee_model.save(using=self.db)
        return user_Employee_model

    def create_user(self, user_employee_user_name, user_employee_password=None, **extra_fields):
        return self._create_user(user_employee_user_name, user_employee_password, False, False, True, **extra_fields)

    def create_superuser(self, user_employee_user_name, user_employee_password=None, **extra_fields):
        return self._create_user(user_employee_user_name, user_employee_password, True, True, True ** extra_fields)
