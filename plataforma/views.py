from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, render


@login_required(login_url="/auth/logar")
def pacientes(request):
    if request.method == "GET":
        return render(request, "pacientes.html")
    elif request.method == "POST":
        nome = request.POST.get("nome")
        sexo = request.POST.get("sexo")
        idade = request.POST.get("idade")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")

        return HttpResponse(f"{nome}, {sexo}, {idade}, {email}, {telefone}")
