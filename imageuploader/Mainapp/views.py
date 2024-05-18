from django.shortcuts import render
from .forms import ImageForm
from .models import Image


def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILE)
        if form.is_valid():
            form.save()
    
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'mainapp/index.html', {'form':form , 'img':img}  )
