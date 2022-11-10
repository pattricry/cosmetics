from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django import forms
from accoutnt.models import Profile



class SignupForm(UserChangeForm):
    username = forms.CharField(max_length=50)
    frist_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password1 = forms.CharField(max_length=50)
    password2 = forms.CharField(max_length=50)

    class meta:
        model = User
        field = ('username', 'frist_name', 'email', 'password1', 'password2')

class PasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=50, widget= forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter old password'}))
    new_password1 =forms.CharField(max_length=50, widget= forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter new password'}))
    new_password2 =forms.CharField(max_length=50, widget= forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter new password'}))

    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')

STATE = [
    ('Aba','aba'),
    ('Bayelsa','bayelsa'),
    ('Edo','edo'),
    ('Delta','dalta'),
    ('Logos','logos'),
]
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name','last_name','email','phone','address','city','state','profile_img')
        widgets ={
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phone number '}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address'}),
            'city': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter City'}),
            'state': forms.Select(attrs={'class':'form-control','placeholder':'Enter State'}, choices=STATE), 
            'profile_img': forms.FileInput(attrs={'class':'form-control'})
        }