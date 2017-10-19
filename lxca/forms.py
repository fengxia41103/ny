# forms.py
from django import forms
from django.forms import ModelForm
from django.forms.widgets import HiddenInput

from lxca.models import *


class AttachmentForm(ModelForm):

    class Meta:
        model = Attachment
        fields = ['description', 'file']


class OrderPduForm(ModelForm):

    class Meta:
        model = OrderPdu
        widgets = {
            "order": HiddenInput(),
            "template": HiddenInput()
        }


class OrderSwitchForm(ModelForm):

    class Meta:
        model = OrderSwitch
        widgets = {
            "order": HiddenInput(),
            "template": HiddenInput()
        }


class OrderServerForm(ModelForm):
    layer0 = forms.ChoiceField(OrderServer.LAYER0_CHOICES)

    class Meta:
        model = OrderServer
        widgets = {
            "order": HiddenInput(),
            "template": HiddenInput()
        }
