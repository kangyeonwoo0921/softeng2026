from django.shortcuts import render, redirect

# Create your views here.
def landing(request):
    return redirect('/blog/')

def about_me(request):
    return render(request, 'single_pages/about_me.html')