from django.shortcuts import render, redirect
from django.forms.utils import ErrorList
from django.conf import settings
from .models import Registration, Guest
from .forms import RegistrationFormSet


# Create your views here.
ctx = {
    "support_email": settings.DEFAULT_WEDDING_EMAIL,
    "website_url": settings.WEDDING_WEBSITE_URL,
    "couple_name": settings.BRIDE_AND_GROOM,
    "wedding_location": settings.WEDDING_LOCATION,
    "wedding_date": settings.WEDDING_DATE,
}


def home(request):
    return render(request, "home.html", ctx)


def register(request):
    queryset = Guest.objects.none()
    if request.method == "POST":
        formset = RegistrationFormSet(data=request.POST)

        if formset.is_valid():
            registration = Registration.objects.create()
            # form_instances = formset.save(commit=False)
            for form in formset:
                guest = Guest(**form.cleaned_data)
                guest.registration = registration
                guest.save()
            # return HttpResponse("Form valid")
            return redirect("wedding-register-success")
        else:
            print("form not valid")
    else:
        formset = RegistrationFormSet(queryset=queryset)
    ctx["formset"] = formset
    return render(request, "partials/registration_form.html", ctx)


def success(request):
    return render(request, "partials/registration_success.html")
