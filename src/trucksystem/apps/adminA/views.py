from django.shortcuts import render
from django.views import View

# Create your views here.
class AdminView(View): 
    def get(self, request): 
        return render(request, 'adminA/index.html')