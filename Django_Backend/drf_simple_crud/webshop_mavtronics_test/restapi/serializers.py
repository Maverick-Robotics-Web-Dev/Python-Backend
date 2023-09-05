from rest_framework import serializers
from .models import UserAdmin


class UserAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAdmin
    fields = ("user_admin_id", "user_admin_name", "user_admin_lastname", "user_admin_user_name", "user_admin_password",
              "user_admin_login", "user_admin_status", "user_admin_status_description", "user_admin_create_at", "user_admin_update_at",)
    read_only_fields = (
        "user_admin_id", "user_admin_create_at", "user_admin_update_at")
