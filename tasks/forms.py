from django import forms
from django.forms import ModelForm

from .models import *
from bootstrap_modal_forms.forms import BSModalForm


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs = {'placeholder':'Task Title...'}))
    descr = forms.CharField(widget = forms.Textarea(attrs = {'rows':4, 'cols':40}))

    class Meta:
        model = Task
        fields = '__all__'

class EditTaskForm(BSModalForm):
    class Meta:
        model = Task
        fields = '__all__'

class DeleteTaskForm(BSModalForm):
    class Meta:
        model = Task
        fields = '__all__'
