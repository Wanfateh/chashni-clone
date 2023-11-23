from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    # email = forms.EmailField(widget=forms.TextInput(attrs={ 'placeholder': 'Enter your Email','class':'login-input'}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder': 'Full Name','class':'login-input'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder': 'Enter your Phone No','class':'login-input'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'login-input'}))


    class Meta:
        model=User
        fields=('full_name','username','password1','password2','phone','city')
    def __init__(self, *args, **kwargs):
        super(SignupForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['username'].widget.attrs['class'] = 'login-input'


        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password1'].widget.attrs['class'] = 'login-input'

        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].widget.attrs['class'] = 'login-input'
        

