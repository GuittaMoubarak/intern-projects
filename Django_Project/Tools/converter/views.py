from django.shortcuts import render
from .models import Editor
from .forms import EditorForm
def index(request):
    form=EditorForm()
    return render(request,'converter/index.html',{'form':form})