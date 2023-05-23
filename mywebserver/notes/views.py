from django.shortcuts import render, redirect
from .models import WeekNote


def week_notes(request):
    week_notes = WeekNote.objects.all()
    context = {'week_notes': week_notes}
    return render(request, 'notes/week_notes.html', context)


def create_week_note(request):
    if request.method == 'POST':
        day_of_week = request.POST['day_of_week']
        note_title = request.POST['note_title']
        note_description = request.POST['note_description']
        WeekNote.objects.create(day_of_week=day_of_week, note_title=note_title, note_description=note_description)
        return redirect('week_notes')
    return render(request, 'notes/create_week_note.html')
