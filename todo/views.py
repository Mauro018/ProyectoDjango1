from django.shortcuts import redirect, render

from todo.forms import TareaForm
from .models import Tarea
# Create your views here.
def index(request):
    tareas = Tarea.objects.all()
    context = {'tareas':tareas}
    return render(request, 'todo/index.html',context)

def agregar(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TareaForm()
    context = {'form':form}
    return render(request,'todo/agregar.html',context)