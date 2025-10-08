from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'UNAVAILABLE'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'UNAVAILABLE'})
    )
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'UNAVAILABLE'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'UNAVAILABLE'})
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'  
