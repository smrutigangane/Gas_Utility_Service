from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    SERVICE_CHOICES = [
        ('repair', 'Repair'),
        ('installation', 'Installation'),
        ('emergency', 'Emergency'),
        ('maintenance', 'Maintenance'),
        ('billing', 'Billing Inquiry'),  # New option added
        ('other', 'Other'),  # New option added
    ]

    # Override the service_type field to use the defined choices
    service_type = forms.ChoiceField(choices=SERVICE_CHOICES, label="Service Type")

    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'description', 'attachment']  
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'service_type': forms.Select(),  # This can be kept as is, since we're providing choices
            'attachment': forms.ClearableFileInput(), 
        }
