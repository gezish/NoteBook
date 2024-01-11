from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Notes


def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html',{'notes': all_notes})# get all notes and send them to a templete


def detail(request,pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note does not exist")    
        
    return render(request, 'notes/notes_detail.html',{'note': note})
    