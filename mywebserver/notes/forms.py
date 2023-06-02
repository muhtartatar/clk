from django import forms
from .models import WeekNote


class WeekNoteForm(forms.ModelForm):
    class Meta:
        model = WeekNote
        fields = ['day_of_week', 'note_title', 'note_description', 'assignee', 'email']

    def clean_assignee(self):
        assignee = self.cleaned_data.get('assignee')
        if assignee and (len(assignee) < 5 or len(assignee) > 100):
            raise forms.ValidationError('Assignee must be between 5 and 100 characters long.')
        return assignee

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not email.endswith('@ithillel.ua'):
            raise forms.ValidationError('Email must be from ithillel.ua domain.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        assignee = cleaned_data.get('assignee')
        email = cleaned_data.get('email')

        if (assignee and not email) or (email and not assignee):
            raise forms.ValidationError('Both assignee and email fields must be provided.')
        return cleaned_data


# views.py
from django.shortcuts import render, redirect
from .forms import WeekNoteForm


def week_notes(request):
    week_notes = WeekNote.objects.all()
    context = {'week_notes': week_notes}
    return render(request, 'notes/week_notes.html', context)


def create_week_note(request):
    if request.method == 'POST':
        form = WeekNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('week_notes')
    else:
        form = WeekNoteForm()
    return render(request, 'notes/create_week_note.html', {'form': form})
