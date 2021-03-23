from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
from .models import Sale
from .forms import SalesSearchForm

def home_view(request):
    form = SalesSearchForm()
    context = {'form':form}

    return render(request, 'sales/index.html', context)


class SaleListView(ListView):
    model=Sale
    template_name='sales/sales-list.html'


class SaleDetailView(DetailView):
    model=Sale
    template_name= 'sales/sales-detail.html'
