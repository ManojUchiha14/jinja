from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'Django', 'age': 2}
    return render(request,'jinja_prints.html',context=d)