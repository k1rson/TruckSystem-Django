from django.shortcuts import render
from django.views import View

# Create your views here.
class FinanceView(View): 
    def get(self, request): 
        return render(request, 'finance/index.html')