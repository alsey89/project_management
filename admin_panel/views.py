from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
# build a user creation route
def index(request):
    return HttpResponse("Hello, world. You're at the admin_panel index.")

def create_organization(request):
    if request.method == "POST":
        organization = models.Organization(org_name=request.POST["org_name"])
        organization.save()
        return HttpResponse("Organization created successfully.")
    return HttpResponse("Hello, world. You're at the admin_panel create_organization.")


