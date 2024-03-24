from django.contrib import admin
from .models import UserProfile,UserTask
from django.contrib.auth.admin import UserAdmin

class CustomUsertask(admin.ModelAdmin):
    list_display=("user","title","status", "created_date")

class CustomUserAdmin(UserAdmin):
    model = UserProfile
    list_display = ("email", "is_staff", "is_active",'is_superuser')
    list_filter = ("email", "is_staff", "is_active",'is_superuser')
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "phone", "date_of_birth", "picture")}),
        ("Permissions", {"fields": ("is_staff",'is_superuser', "is_active", "groups", "user_permissions")}),
    )  
    add_fieldsets = (
        (None, {
            "classes": ("collapse",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active",'is_superuser', "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(UserProfile,CustomUserAdmin)



admin.site.register(UserTask,CustomUsertask)