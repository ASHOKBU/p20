from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
import re
def validate_name(name):
    if len(name)>10:
        raise ValidationError("Name is not valide")
    return name

class SampleForm(forms.Form):
    name=forms.CharField(max_length=100,required=True,label="Name: ",validators=[validate_name])
    email=forms.EmailField(max_length=100, required=True,label="Email: ",validators=[validators.MinLengthValidator(5)])
    confirm_email=forms.EmailField(max_length=100, required=True,label="Confirm Email:")
    pwd=forms.CharField(max_length=20, required=True, label="Password",widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
    profile_pic=forms.ImageField(max_length=200,required=True,label="Profile Pic")
    botcacher= forms.CharField(max_length=10, required=False,widget=forms.HiddenInput)

    def clean(self,*args, **kwargs):
        cleaned_data= super().clean()#getting all data in the filled form
        email= cleaned_data.get('email')
        cemail= cleaned_data.get('confirm_email')
        if email == cemail:
            return cleaned_data
        self.add_error('confirm_email',"Both emails are not same")#this method will decide to which field we need to show error
    
    def clean_name(self):
        name=self.cleaned_data.get("name")
        for i in name:
            if not ('a'<=i<='z' or 'A'<=i<='Z'):
                raise ValidationError("Name must contain only alphabets")
        return name

    def clean_botcacher(self):
        data=self.cleaned_data.get("botcacher")
        if len(data)==0:
            return data
        self.add_error("name","Computer Error")