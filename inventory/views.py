from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone

from .models import Axie, Transaction 

# Create your views here.
def dashboard_view(request):
    listed_axies = Axie.objects.filter(status='Listed').count()

    sold_axies = Axie.objects.filter(status='Sold', sell_date__month=timezone.now().month)

    monthly_profit = sum([axie.profit() for axie in sold_axies if axie.profit() is not None])

    context = { 
        'listed_axies': listed_axies,
        'monthly_profit': monthly_profit,
        'sold_axies': sold_axies.count()
    }

    return render(request, 'dashboard.html', context)

def axie_list_view(request):
    axies = Axie.objects.filter(
        Q(status='Owned') | Q(status='Listed')
    ).order_by('axie_id')

    context = {
        'axies': axies
    }
    return render(request, 'axie-list.html', context)

def add_axie_form_view(request):
    if request.method == 'POST':
        fields = ['axieID', 'breedCount', 'purchasePrice', 'purchaseDate', 'status']
        data = {field: request.POST.get(field) for field in fields}

        if Axie.objects.filter(axie_id=data['axieID']).exists():
            messages.info(request, 'Axie already exists.')
            return render(request, 'axie-form.html')
        
        axie_data = {
            'axie_id': data['axieID'],
            'breed_count': data['breedCount'],
            'purchase_price': data['purchasePrice'],
            'purchase_date': data['purchaseDate'],
            'status': data['status']
        }

        axie = Axie.objects.create(**axie_data)

        record_transaction(axie, axie_data['status'], axie_data['purchase_date'])

        messages.success(request, 'Axie added successfully.')

        # Stop here for now
    return render(request, 'axie-form.html')

def edit_axie_form_view(request, axie_id):
    try:
        axie = Axie.objects.get(axie_id=axie_id)
        if request.method == 'POST':
            fields = ['breedCount', 'purchasePrice', 'purchaseDate', 'sellingPrice', 'dateSold', 'status']
            data = {field: request.POST.get(field) for field in fields}

            axie_data = {
                'breed_count': data['breedCount'],
                'purchase_price': data['purchasePrice'],
                'purchase_date': data['purchaseDate'],
                'selling_price': data['sellingPrice'],
                'sell_date': data['dateSold'],
                'status': data['status']
            }

            if axie_data['status'] == 'Sold':
                record_transaction(axie, axie_data['status'], axie_data['sell_date'])

            Axie.objects.filter(axie_id=axie_id).update(**axie_data)

            messages.success(request, 'Axie updated successfully.')
        
        context = {
            'axie': axie 
        }

        return render(request, 'axie-form.html', context)
    except Axie.DoesNotExist:
        return HttpResponse('Axie not found.')

def record_transaction(axie, transaction_type, date):
    Transaction.objects.create(
        axie = axie,
        transaction_type = transaction_type,
        date = date
    )

def transaction_list_view(request):
    transactions = Transaction.objects.all().order_by('-date')

    context = {
        'transactions': transactions
    }
    return render(request, 'transactions.html', context)

