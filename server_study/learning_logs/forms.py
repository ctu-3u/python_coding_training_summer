from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['subject','text']
        labels = {'subject':'Name','text':'Description'}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}