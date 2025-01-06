from django.shortcuts import render
from .models import RubberType

def stock_overview(request):
    rubber_types = RubberType.objects.all()
    return render(request, 'ledger/stock_overview.html', {'rubber_types': rubber_types})
