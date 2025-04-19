from django.shortcuts import render
from .models import Tarea

# Create your views here.
def index(request):
    tareas = Tarea.objects.all()
    context = {'tareas':tareas}
    return render(request, 'Todo/index.html',context)

