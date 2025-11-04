from django.shortcuts import render
from .models import Note

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

def note_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})

def note_create(request):
    if request.method == 'POST':
        # Logic for creating a new note
        pass
    return render(request, 'notes/note_form.html')

def note_update(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        # Logic for updating the note
        pass
    return render(request, 'notes/note_form.html', {'note': note})

def note_delete(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        note.delete()
        # Redirect after deletion
    return render(request, 'notes/note_confirm_delete.html', {'note': note})