#import datetime
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime
from django.forms.widgets import CheckboxSelectMultiple, HiddenInput
from main.models import Perfil, Lista, Consulta
#BIRTH_YEAR_CHOICES = [(i, i) for i in range(1950, 2012)]


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        exclude = ("user", 'folio')
        widgets = {
            'cumpleanios': AdminDateWidget(),
        }


class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ('nombre',)


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ('fecha_hora', 'lugar', 'tpx', 'px', 'consultor')
        widgets = {
            'fecha_hora': AdminSplitDateTime(),
            'px': CheckboxSelectMultiple(),
            'tpx': HiddenInput(),
            'consultor': HiddenInput(),
        }
