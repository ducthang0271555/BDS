from django.shortcuts import render
from .models import Property

def property_detail(request, property_id):
    property = Property.objects.get(id=property_id)
    return render(request, 'listings/property_detail.html', {'property': property})

def property_list(request):
    query = request.GET.get('q')
    if query:
        properties = Property.objects.filter(name__icontains=query)
    else:
        properties = Property.objects.all()
    return render(request, 'listings/property_list.html', {'properties': properties})
