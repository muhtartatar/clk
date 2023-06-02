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



