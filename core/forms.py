from django import forms


# options on HTML form
OPTION_CHOICES = [
    ("general", "General Inquiry"),
    ("support", "Support"),
    ("feedback", "Feedback"),
    ("other", "Other"),
]


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100, label="Full Name")
    email = forms.EmailField(label="Email")
    option = forms.ChoiceField(choices=OPTION_CHOICES, label="Select Option")
    message = forms.CharField(widget=forms.Textarea, label="Message")
