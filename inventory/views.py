from django.shortcuts import render, HttpResponse
from .models import Axie, Transaction 
from django.contrib import messages

# Create your views here.
def dashboard_view(request):
    return render(request, 'dashboard.html')

def axie_list_view(request):
    axies = Axie.objects.all().order_by('axie_id')

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

        Axie.objects.create(**axie_data)
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

            Axie.objects.filter(axie_id=axie_id).update(**axie_data)

            messages.success(request, 'Axie updated successfully.')
        
        context = {
            'axie': axie 
        }

        return render(request, 'axie-form.html', context)
    except Axie.DoesNotExist:
        return HttpResponse('Axie not found.')

def transaction_list_view(request):
    transactions = Transaction.objects.all().order_by('date')

    context = {
        'transactions': transactions
    }
    return render(request, 'transactions.html', context)

