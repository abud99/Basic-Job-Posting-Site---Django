from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField
from django.contrib.auth.decorators import login_required
from .models import job

LANGUAGES = [
    ('eng', 'English'),
    ('arb', 'Arabic'),
    ('oth', 'Other'),
]


class CustomRegister(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    #country = CountryField().formfield()
    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name',  'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].help_text = ''
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        

    # title = models.CharField(max_length=100)
    # userID = models.ForeignKey(freelance, on_delete=models.CASCADE)
    # status = models.CharField(max_length=30)
    # price = models.FloatField()
    # language = models.CharField(max_length=30, null=True)
    # description = models.TextField()







