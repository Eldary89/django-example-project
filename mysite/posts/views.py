import datetime

from django.shortcuts import render
from django.utils import timezone

from .models import Users
from .forms import UsersForm

# Create your views here.
def index(request):
    context = {}
    return render(request, 'posts/index.html', context)

def register(request):
    if request.method == 'POST':
        user = Users(registered_time=timezone.now())
        form = UsersForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'posts/index.html')
        else:
            print("Not Uploaded")
    else:
        form = UsersForm()
    return render(request, 'posts/register.html', {'form':form})
