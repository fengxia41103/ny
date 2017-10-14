# forms.py
from django import forms
from django.forms import ModelForm
from django.forms.widgets import HiddenInput

from lxca.models import *


class AttachmentForm(ModelForm):

    class Meta:
        model = Attachment
        fields = ['description', 'file']