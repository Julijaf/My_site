from django.forms import ModelForm, TextInput, Textarea
from django import forms
from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'msg']
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.CharField(label='Your email', max_length=100)
    subject = forms.CharField(label='subject', max_length=100)
    message = forms.CharField(label='message', max_length=400)