from django import forms
from django.forms import ModelForm

from .models import *
from bootstrap_modal_forms.forms import BSModalForm


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs = {'placeholder':'Task Title...'}))

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

class LineForm(ModelForm):
    class Meta:
        model = TaskLine
        fields = '__all__'
