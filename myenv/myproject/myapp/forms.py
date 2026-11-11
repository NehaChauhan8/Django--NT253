from django import forms

class InputForm1(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())



# class InputForm2(forms.Form):
#     name=forms.CharField()
#     email=forms.EmailField()
#     password=forms.CharField(widget=forms.PasswordInput())
#     age=forms.IntegerField()#for number input field
#     dob=forms.DateField(widget=forms.DateInput()) #for date input field
#     gender=forms.CharField( #for  radio buttons or a dropdown menu
#         choices=[
#             ('M', 'Male'),
#             ('F', 'Female'),
#             ('O', 'Other'),
#         ]
#     )
#     address=forms.CharField(widget=forms.Textarea()) #for multi-line input and textarea
#     profile_picture=forms.ImageField(required=False) #for file upload field
#     website=forms.URLField(required=False) #for URL input field
#     agree=forms.BooleanField(required=False) #for terms and conditions checkbox


class InputForm2(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    age = forms.IntegerField()
    birthdate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': '2000-01-01','max': '2010-12-31'}))
    gender = forms.ChoiceField(
        choices=[
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other')
        ]
    )
    address = forms.CharField(widget=forms.Textarea)
    profile_picture = forms.ImageField(required=False)
    website = forms.URLField(required=False)
    agree = forms.BooleanField(required=False)


from django import forms
from .models import Blogpost
class Blogpostform(forms.ModelForm):
    class Meta:
        model=Blogpost
        fields='__all__'
        