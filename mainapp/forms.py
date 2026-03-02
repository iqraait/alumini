
from django import forms
from .models import AlumniRegistration, Department

class AlumniRegistrationForm(forms.ModelForm):
    class Meta:
        model = AlumniRegistration
        fields = [
            'full_name', 'country', 'iqraa_no', 'phone_number',
            'whatsapp_number', 'email', 'indian_address',
            'father_name', 'father_iqraa_num', 'father_address',
            'mother_name', 'mother_iqraa_num', 'mother_address',
            'spouse_name', 'spouse_iqraa_num', 'spouse_address',
            'children',
            'tenure_from', 'tenure_to', 'iqraa_designation',
            'iqraa_department', 'iqraa_campus', 'memorable_experience',
            'current_city', 'professional_field', 'alumni_activities_interest',
        ]
        
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'iqraa_no': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+966501234567'}),
            'whatsapp_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+966501234567'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'indian_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'father_iqraa_num': forms.TextInput(attrs={'class': 'form-control'}),
            'father_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Complete address with city, state, pincode'}),
            
            'mother_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_iqraa_num': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Complete address with city, state, pincode'}),
            
            'spouse_name': forms.TextInput(attrs={'class': 'form-control'}),
            'spouse_iqraa_num': forms.TextInput(attrs={'class': 'form-control'}),
            'spouse_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Complete address with city, state, pincode'}),
            
            'children': forms.HiddenInput(),
            
            'tenure_from': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tenure_to': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'iqraa_designation': forms.TextInput(attrs={'class': 'form-control'}),
            'iqraa_department': forms.Select(attrs={'class': 'form-control'}),
            'iqraa_campus': forms.TextInput(attrs={'class': 'form-control'}),
            'memorable_experience': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'current_city': forms.TextInput(attrs={'class': 'form-control'}),
            'professional_field': forms.TextInput(attrs={'class': 'form-control'}),
            'alumni_activities_interest': forms.Select(attrs={'class': 'form-control'}),

        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['iqraa_department'].queryset = Department.objects.all()
        
        
        # Required fields
        required_fields = [
            'full_name', 'whatsapp_number', 'email',
            'father_name', 'mother_name',
            'indian_address', 'tenure_from', 'tenure_to',
            'country', 'current_city', 'professional_field',
        ]
        
        for field_name in required_fields:
            self.fields[field_name].required = True
            self.fields[field_name].widget.attrs['required'] = 'required'
        
        # Make conditional fields not required by default
        conditional_fields = ['father_address', 'mother_address', 'spouse_address']
        for field_name in conditional_fields:
            self.fields[field_name].required = False
        
        # Add help texts
        self.fields['father_address'].help_text = "Required only if Father's Iqraa number is not provided"
        self.fields['mother_address'].help_text = "Required only if Mother's Iqraa number is not provided"
        self.fields['spouse_address'].help_text = "Required only if Spouse's Iqraa number is not provided"
    
    def clean(self):
        cleaned_data = super().clean()
        
        # Father's condition
        father_iqraa = cleaned_data.get('father_iqraa_num')
        father_address = cleaned_data.get('father_address')
        if not father_iqraa and not father_address:
            self.add_error('father_address', 'Please provide either Father\'s Iqraa number OR complete address')
            self.add_error('father_iqraa_num', 'Either provide Iqraa number or address')
        
        # Mother's condition
        mother_iqraa = cleaned_data.get('mother_iqraa_num')
        mother_address = cleaned_data.get('mother_address')
        if not mother_iqraa and not mother_address:
            self.add_error('mother_address', 'Please provide either Mother\'s Iqraa number OR complete address')
            self.add_error('mother_iqraa_num', 'Either provide Iqraa number or address')
        
        # Spouse condition (only if spouse name is provided)
        spouse_name = cleaned_data.get('spouse_name')
        spouse_iqraa = cleaned_data.get('spouse_iqraa_num')
        spouse_address = cleaned_data.get('spouse_address')
        
        if spouse_name:  # If spouse name is filled
            if not spouse_iqraa and not spouse_address:
                self.add_error('spouse_address', 'Please provide either Spouse\'s Iqraa number OR complete address')
                self.add_error('spouse_iqraa_num', 'Either provide Iqraa number or address')
        
        # Validate tenure dates
        tenure_from = cleaned_data.get('tenure_from')
        tenure_to = cleaned_data.get('tenure_to')
        if tenure_from and tenure_to and tenure_from > tenure_to:
            self.add_error('tenure_to', '"To" date must be after "From" date')
        
        return cleaned_data











