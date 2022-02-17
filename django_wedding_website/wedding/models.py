from django.db import models
from uuid import uuid4

# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class DefaultManager(models.Manager):
    pass


class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()


class RootModel(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)


class BaseModel(RootModel):
    class Meta:
        abstract = True
        default_manager_name = "default_manager"

    objects = CustomManager()
    default_manager = DefaultManager()

    modified = models.DateTimeField(auto_now=True, editable=False)


# from phonenumber_field.modelfields import PhoneNumberField
MEALS = [
    ("beef", "Minced meat patties (Fleischlaibchen)"),
    ("fish", "Char (Saibling, Fish)"),
    ("vegetarian", "Vegetarian dumpling tris"),
    ("child", "Children's menu: Schnitzel"),
]


class Registration(BaseModel):
    """
    A registration consists of one or more guests.
    """

    # name = models.TextField()
    def __str__(self):
        return f"Registration: {self.id}"


class Guest(BaseModel):
    """
    A single guest
    """

    registration = models.ForeignKey("Registration", on_delete=models.CASCADE)
    first_name = models.TextField(help_text="First Name")
    last_name = models.TextField(help_text="Last Name")
    is_attending = models.BooleanField(null=True, default=True)
    meal = models.CharField(max_length=46, choices=MEALS, null=True, blank=True)
    is_child = models.BooleanField(default=False)
    comments = models.TextField(
        blank=True, help_text="Anything else we should know about?"
    )

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"Guest: {self.name}"
