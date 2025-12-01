from django.shortcuts import render

# Create your views here.
def news_veiw(request):
    context={
        'new':'Asliddin'
    }
    return render(request, 'index.html',context)