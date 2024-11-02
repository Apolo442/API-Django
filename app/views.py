# views.py
from django.shortcuts import redirect, render
from app.forms import PacienteForm
from django.http import HttpResponseServerError
from app.models import Paciente
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Paciente.objects.filter(nome__icontains=search)
    else:
        data['db'] = Paciente.objects.all()
    
    #all = Paciente.objects.all()
    #paginator = Paginator(all, 99)
    #pages = request.GET.get('page')
    #data['db'] = paginator.get_page(pages)
    
    return render(request, 'index.html', data)    


def form(request):
    data = {}
    data['form'] = PacienteForm()
    return render(request, 'form.html', data)


def create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            print("FORMULÁRIO SALVO")
            return redirect('home')
        else:
            print("ERRO AO SALVAR FORMULÁRIO")
            # Se o formulário não for válido, renderize novamente a página do formulário com mensagens de erro.
            return render(request, 'form.html', {'form': form})
    else:
        # Se o método não for POST, apenas redirecione para a home ou outra página desejada.
        return redirect('home')
    
def view(request, pk):
    data = {}
    data['db'] = Paciente.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Paciente.objects.get(pk=pk)
    data['form'] = PacienteForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Paciente.objects.get(pk=pk)
    form = PacienteForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
    
def delete(request, pk):
    db = Paciente.objects.get(pk=pk)
    db.delete()
    return redirect('home')