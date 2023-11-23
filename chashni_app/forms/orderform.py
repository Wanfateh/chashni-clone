from django import forms
from ..models import Order


class OrderForm( forms.ModelForm ):

    class Meta:
        model=Order
        fields=('__all__')
        exclude = ('user', 'order_amount', 'payment_mod','delivery_method')

    
    def __init__(self, *args, **kwargs):
        super(OrderForm,self).__init__(*args, **kwargs)

        self.fields['full_name'].widget.attrs['placeholder'] = 'Enter your full name'
        self.fields['address'].widget.attrs['placeholder'] = 'Write your complete address.....'
        self.fields['address'].widget.attrs['coloumn'] = 'cols_20'
        self.fields['address'].widget.attrs['rows'] = '3'


        # self.fields['city'].widget.attrs['placeholder'] = 'form-control nav-search'
        self.fields['phone'].widget.attrs['placeholder'] = 'Your contact number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email address'
        self.fields['instructions'].widget.attrs['placeholder'] = 'Write your message here.....'


