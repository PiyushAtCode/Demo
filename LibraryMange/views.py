from django.shortcuts import render

# Create your views here.


def show_home(request):
    return render(request, 'home.html')


def two_sum(request):
    result = None 
    
    if request.method == "POST":
        a = int(request.POST.get("num1", 0))
        b = int(request.POST.get("num2", 0))
        
        result = a + b 
    
    return render(request , 'home.html' , {"result":result})
    
    
def home(request):
    return render(request, "home.html")

