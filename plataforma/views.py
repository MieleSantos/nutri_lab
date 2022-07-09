from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, render


@login_required(login_url="/auth/logar")
def pacientes(request):
    return render(request, "plataforma.html")
