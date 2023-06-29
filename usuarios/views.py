from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            messages.error(request, 'Digite duas senhas iguais.')
        elif not all([nome, email, senha, confirmar_senha]):
            messages.error(request, 'Preencha todos os campos.')
        else:
            try:
                User.objects.create_user(
                    username=nome,
                    email=email,
                    password=senha,
                )
                messages.success(request, 'Usuário criado com sucesso.')
            except Exception as e:
                messages.error(request, f'Erro interno do sistema: {str(e)}')

        return render(request, 'cadastro.html')
def logar(request):
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')
    if request.method == "GET":
        return render(request, 'login.html')
    
    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = authenticate(username=nome,
                            password=senha)

        if user is not None:
            login(request, user)
            return redirect('/divulgar/novo_pet')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'login.html')
def sair(request):
    logout(request)
    return redirect('/auth/login')