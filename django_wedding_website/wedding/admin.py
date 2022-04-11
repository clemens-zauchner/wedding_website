from django.contrib import admin
from .models import Guest, Registration

# Register your models here.


class RootAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)


class BaseAdmin(RootAdmin):
    readonly_fields = (
        "created",
        "modified",
    )


class GuestInline(admin.TabularInline):
    model = Guest
    fields = (
        "registration",
        "first_name",
        "last_name",
        "is_attending",
        "meal",
        "is_child",
        "comments",
    )
    readonly_fields = (
        "registration",
        "first_name",
        "last_name",
    )
    extra = 1


@admin.register(Guest)
class GuestAdmin(BaseAdmin):
    ordering = ("created",)
    list_display = ("registration", "first_name", "last_name")
    list_filter = ("is_attending", "is_child", "meal")

    # def registration_id(self, obj):
    #     return obj.registration.id


@admin.register(Registration)
class RegistrationAdmin(BaseAdmin):
    list_display = ["id"]
    inlines = [
        GuestInline,
    ]
