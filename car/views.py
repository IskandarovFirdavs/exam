from django.shortcuts import render
from car.models import DateModel

def pricing_view(request):
    records = DateModel.objects.filter(price__gt=100)
    
    context = {
        'records': records
    }
    
    return render(request, 'index.html', context)
