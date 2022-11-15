from django import forms
from .models import DetallePago


class DetallePagoForm(forms.ModelForm):
    class Meta:
        model = DetallePago
        fields = ['forma_pago', 'cliente', 'banco', 'titular', 'cc_titular', 'total_pago', 'iva_pago',]
        widgets = {
            'forma_pago' : forms.Select(attrs = {'class': 'form-select'}),
            'cliente' : forms.TextInput(attrs = {'class': 'form-control', 'id': 'id_cliente', 'name': 'id_cliente', 'value': 'cliente'}),
            'banco' : forms.Select(attrs = {'class': 'form-select'}),
            'titular' : forms.TextInput(attrs = {'class': 'form-control'}),
            'cc_titular' : forms.TextInput(attrs = {'class': 'form-control'}),
            'total_pago' : forms.TextInput(attrs = {'class': 'form-control', 'id': 'id_total_pago', 'name': 'id_total_pago'}),
            'iva_pago' : forms.TextInput(attrs = {'class': 'form-control'})
        }
        #exclude = ['create_at', 'modify_at',]