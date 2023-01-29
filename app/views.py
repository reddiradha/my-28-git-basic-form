from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def form_html(request):
    return render(request,'form_html.html')
