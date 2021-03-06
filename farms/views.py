from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Farm
from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def index(request):
    context = {
    }
    return render(request, 'farm/index.html',context)

class FarmListado(LoginRequiredMixin,ListView): 
    model = Farm
 
class FarmDetalle(LoginRequiredMixin,DetailView): 
    model = Farm
 
class FarmCrear(LoginRequiredMixin,SuccessMessageMixin, CreateView): 
    model = Farm
    form = Farm
    fields = "__all__" 
    success_message = 'Granja Creada Creada Correctamente !' 
 
    def get_success_url(self):        
        return reverse('leer_farm') 
 
class FarmActualizar(LoginRequiredMixin,SuccessMessageMixin, UpdateView): 
    model = Farm
    form = Farm
    fields = "__all__"  
    success_message = 'Granja Actualizada Correctamente !' 
 
    def get_success_url(self):               
        return reverse('leer_farm')  
 
class FarmEliminar(LoginRequiredMixin,SuccessMessageMixin, DeleteView): 
    model = Farm 
    form = Farm
    fields = "__all__"     
 
    def get_success_url(self): 
        success_message = 'Granja Eliminado Correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('leer_farm') 