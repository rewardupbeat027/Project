from django.db.models import Q
from django.shortcuts import render
import time
from .models import Humans, Auto


# Create your views here.
def main(request):
    return render(request, "main.html")

def human(request):
    human = Humans.objects.all()
    return render(request, 'human.html', {'human': human})

def auto(request):
    auto = Auto.objects.all()
    return render(request, 'auto.html', {'auto': auto})

def SearchResultsView(request):
    query = request.GET.get('q')
    human = Humans.objects.all().filter(
        Q(name__icontains=query)
    )
    return render(request, 'human.html', {'human': human})

def SearchResultsViewauto(request):
    start_time = time.time()
    query = request.GET.get('q')
    auto = Auto.objects.all().filter(
        Q(text1__icontains=query)
    )
    end_time = time.time()
    elapsed_time = end_time - start_time
    return render(request, 'auto.html', {'auto': auto, 'elapsed_time': elapsed_time})