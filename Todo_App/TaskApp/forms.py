from django import forms
from .models import TaskDetails



class TaskForm(forms.ModelForm):

    class Meta:
        model = TaskDetails
        fields = '__all__'