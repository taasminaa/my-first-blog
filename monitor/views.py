from django.shortcuts import render

# Create your views here.
def index (request):
    mydict = {'value1':'Health Monitoring System'}
    return render(request, 'monitor/index.html', context = mydict)
