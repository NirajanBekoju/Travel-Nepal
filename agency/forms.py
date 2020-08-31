from django import forms
from .models import Event

class AddEventForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class' : 'form-control'}
            )
        )
    description = forms.CharField(widget=forms.Textarea(
        attrs={'class' : 'form-control'}
    ))

    image = forms.ImageField(widget=forms.FileInput(
        attrs={'class':'form-control'}
    ))
    location = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    booking_date_limit = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    
    class Meta:
        model = Event    
        fields = ['title', 'description', 'image', 'location', 'booking_date_limit']
