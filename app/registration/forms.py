from django import forms
from .models import Event

class EventForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["event"].queryset = Event.objects.all()

    event = forms.ModelMultipleChoiceField(queryset=None, label="Выберите событие")