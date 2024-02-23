from django.shortcuts import render
from . models import movie_details
# Create your views here.

def Home(request):
    movie_de=movie_details.objects.all()
   
    return render(request,'home.html',{'movie':movie_de})

def Create(request):
    
    if request.POST:
        title=request.POST.get('title')
        year=request.POST.get('year')
        summery=request.POST.get('summery')
        
        obj_movie=movie_details(Name=title,Year=year, discription=summery)
        obj_movie.save()

        
    return render(request,'create.html')

def Edit(request):
    return render(request,'edit.html')