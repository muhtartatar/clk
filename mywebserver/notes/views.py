from django.shortcuts import render, redirect
from .forms import WeekNoteForm
from .models import WeekNote
from validate_email_address import validate_email


def week_notes(request):
    week_notes = WeekNote.objects.all()
    context = {'week_notes': week_notes}
    return render(request, 'notes/week_notes.html', context)


def create_week_note(request):
    if request.method == 'POST':
        form = WeekNoteForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if validate_email(email):
                return redirect('week_notes')
            else:
                form.add_error('email', 'Недійсна електронна пошта')
    else:
        form = WeekNoteForm()
    return render(request, 'notes/create_week_note.html', {'form': form})