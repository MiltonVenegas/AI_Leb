from django.shortcuts import render
from django.views import View
# Create your views here.
class indexView(View):
    def get(self, request):
        return render(request, 'LB.html')