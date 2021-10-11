from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView


from .forms import MascotaForm
from .models import Mascota

# Create your views here.

def index(request):
    return render(request, 'mascota/mascota_list.html')

def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect("mascota_listar")
    else:
        form = MascotaForm()
    return render(request, 'mascota/mascota_form.html', {'form': form})

def mascota_list(request):
    mascota = Mascota.objects.all()
    contexto = {'mascotas':mascota}
    return render(request, 'mascota/mascota_list.html',contexto)

def mascota_list_images(request):
    mascota = Mascota.objects.all()
    contexto = {'mascotas':mascota}
    return render(request, 'mascota/mascota_listar_imagenes.html',contexto)

def mascota_edit(request, folio_mascota):
    mascota = Mascota.objects.get(folio = folio_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, files=request.FILES,instance = mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota_listar')
    return render(request, 'mascota/mascota_form.html',{'form':form})

def mascota_delete(request, folio_mascota):
    mascota = Mascota.objects.get(folio = folio_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota_listar')
    return render(request, 'mascota/mascota_delete.html',{'mascota':mascota})
