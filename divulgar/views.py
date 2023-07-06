from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse 
from . import views
from django.contrib.auth.decorators import login_required
from . models import Tag, Raca, Pet 



@login_required
def novo_pet(request):
   if request.method == "GET":
      tags = Tag.objects.all()
      racas = Raca.objects.all()
      return render(request, 'novo_pet.html', {'tags':tags, 'racas': racas})

   elif request.method == "POST":
         foto = request.FILES.get('foto')
         nome = request.POST.get('nome')
         descricao = request.POST.get('descricao')
         estado = request.POST.get('estado')
         cidade = request.POST.get('cidade')
         telefone = request.POST.get('telefone')
         tags = request.POST.getlist('tags')
         raca = request.POST.get('raca')

 #TODO: Validar dados

         pet = Pet(
            usuario=request.user,
            foto=foto,
            nome=nome,
            descricao=descricao,
            estado=estado,
            cidade=cidade,
            telefone=telefone,
            raca_id=raca,
      )

         pet.save()
        
         for tag_id in tags:
             tag = Tag.objects.get(id=tag_id)
             pet.tags.add(tag)

         pet.save()

         tags = Tag.objects.all()
         racas = Raca.objects.all()
         messages.add_message(request, constants.SUCCESS, 'Novo pet cadastrado')
         return render(request, 'novo_pet.html', {'tags': tags, 'racas': racas})
        