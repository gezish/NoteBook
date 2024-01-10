from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from .models import Notes


def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html',{'notes': all_notes})# get all notes and send them to a templete