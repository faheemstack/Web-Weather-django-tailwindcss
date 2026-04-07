from django import forms
from django.contrib.auth.models import User
from .models import CustomUser


# options on HTML form
OPTION_CHOICES = [
    ("general", "General Inquiry"),
    ("support", "Support"),
    ("feedback", "Feedback"),
    ("other", "Other"),
]
ALLOWED_TYPES = ['jpg', 'jpeg', 'png', 'svg']


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100, label="Full Name")
    email = forms.EmailField(label="Email")
    option = forms.ChoiceField(choices=OPTION_CHOICES, label="Select Option")
    message = forms.CharField(widget=forms.Textarea, label="Message")

class RegisterForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['full_name','email','password','profile_image']
