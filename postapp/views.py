from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view_hello_world(request):
    return HttpResponse("<h1>Hello world</h1>")


def view_hello_world_template(request):
    database_data="Ram"
    database_data_lists=["shyam","hari","gita"]
    context_variable={
        'name' :database_data,
        'names' :database_data_lists
    }
    return render(request,'index.html',context_variable)