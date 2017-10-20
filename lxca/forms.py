# forms.py
from django import forms
from django.forms import ModelForm
from django.forms.widgets import HiddenInput


from lxca.models import *
from lxca.catalog_models import *
from lxca.architect_models import *
from lxca.order_models import *
from lxca.mfg_models import *


class AttachmentForm(ModelForm):

    class Meta:
        model = Attachment
        fields = ['description', 'file']


class OrderPduForm(ModelForm):

    class Meta:
        model = OrderPdu
        exclude = ["order", "template"]


class OrderSwitchForm(ModelForm):

    class Meta:
        model = OrderSwitch
        exclude = ["order", "template"]


class OrderServerForm(ModelForm):
    layer0 = forms.ChoiceField(OrderServer.LAYER0_CHOICES)

    class Meta:
        model = OrderServer
        exclude = ["order", "template", ]


class MfgPduForm(ModelForm):

    class Meta:
        model = MfgPdu
        exclude = ["mfg", "uuid", "order"]


class MfgSwitchForm(ModelForm):

    class Meta:
        model = MfgSwitch
        exclude = ["mfg", "uuid", "order"]


class MfgServerForm(ModelForm):

    class Meta:
        model = MfgServer
        exclude = ["mfg", "uuid", "order"]
