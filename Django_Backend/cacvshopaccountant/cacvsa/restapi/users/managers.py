from typing import Self
from django.db.models import Manager
from django.contrib.auth.models import BaseUserManager

from .models import UserEmployeeModel


class UserEmployeeManager(BaseUserManager, Manager):

    def _create_user(self: Self, user_name: str, password: str, is_staff: bool, is_superuser: bool, is_active: bool, **extra_fields: dict) -> UserEmployeeModel:

        user_employee_model: UserEmployeeModel = None

        user_employee_model = self.model(
            user_name=user_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user_employee_model.set_password(password)
        user_employee_model.save(using=self.db)

        return user_employee_model

    def create_user(self: Self, user_name: str, password: str, **extra_fields: dict) -> UserEmployeeModel:
        return self._create_user(user_name, password, False, False, True, **extra_fields)

    def create_superuser(self: Self, user_name: str, password: str, **extra_fields: dict) -> UserEmployeeModel:
        return self._create_user(user_name, password, True, True, True, ** extra_fields)
