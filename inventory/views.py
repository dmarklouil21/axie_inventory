from django.shortcuts import render

# Create your views here.
def dashboard_view(request):
    return render(request, 'dashboard.html')

def axie_list_view(request):
    return render(request, 'axie-list.html')

def add_axie_view(request):
    return render(request, 'axie-form.html')

def transaction_list_view(request):
    return render(request, 'transactions.html')