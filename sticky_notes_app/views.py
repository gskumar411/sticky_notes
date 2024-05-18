"""Module for views."""
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm

def note_list(request):
    """
    View to list all notes.
    """
    notes = Note.objects.all()
    return render(request, 'sticky_notes_app/note_list.html', {'notes': notes})

def note_detail(request, pk):
    """
    View to display the details of a single note.
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'sticky_notes_app/note_detail.html', {'note': note})

def note_new(request):
    """
    View to create a new note.
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'sticky_notes_app/note_edit.html', {'form': form})

def note_edit(request, pk):
    """
    View to edit an existing note.
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'sticky_notes_app/note_edit.html', {'form': form})

def note_delete(request, pk):
    """
    View to delete a note.
    """
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_list')
