

from django.core.validators import RegexValidator
from django.db import models


class Department(models.Model):
    """
    Master table for departments - makes it easy to add/edit departments
    without changing code
    """
    name = models.CharField(max_length=200, unique=True, verbose_name="Department Name")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = "Department"
        verbose_name_plural = "Departments"
    
    def __str__(self):
        return self.name



class AlumniRegistration(models.Model):
    # ========== CHOICE CONSTANTS ==========
    # Country Choices
    SAUDI_ARABIA = 'Saudi Arabia'
    UAE = 'United Arab Emirates'
    KUWAIT = 'Kuwait'
    QATAR = 'Qatar'
    OMAN = 'Oman'
    BAHRAIN = 'Bahrain'
    
    COUNTRY_CHOICES = [
        (SAUDI_ARABIA, 'Saudi Arabia'),
        (UAE, 'United Arab Emirates'),
        (KUWAIT, 'Kuwait'),
        (QATAR, 'Qatar'),
        (OMAN, 'Oman'),
        (BAHRAIN, 'Bahrain'),
    ]
    HEAR_ABOUT_CHOICES = [
    ('social_media', 'Social Media'),
    ('twitter', 'Twitter'),
    ('friend', 'Friend or Family'),
    ('colleague', 'Colleague'),
    ('alumni_event', 'Alumni Event'),
    ('other', 'Other'),
]
    
    # Department Choices
    DEPARTMENT_CHOICES = [
        ('Administration', 'Administration'),
        ('Doctor', 'Doctor'),
        ('Nurse', 'Nurse'),
        ('Other', 'Other'),
    ]
    
    # Activity Interest Choices
    ACTIVITY_INTEREST_CHOICES = [
        ('Yes', 'Yes'),
        ('Maybe', 'Maybe'),
        ('No', 'No'),
    ]
    
    # ========== PERSONAL INFORMATION ==========
    full_name = models.CharField(max_length=200, verbose_name="Full Name")
    country = models.CharField(
        max_length=100,
        choices=COUNTRY_CHOICES,
        verbose_name="Country of Residence"
    )
    iqraa_no = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Iqraa Number"
    )
    phone_number = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Phone number must be entered in format: '+999999999'. Up to 15 digits allowed.")],
        verbose_name="Phone Number"
    )
    whatsapp_number = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="WhatsApp number must be entered in format: '+999999999'.")],
        verbose_name="WhatsApp Number"
    )
    email = models.EmailField(unique=True, verbose_name="Email Address")
    indian_address = models.TextField(verbose_name="Indian Address")
    
    # ========== FATHER'S INFORMATION ==========
    father_name = models.CharField(max_length=200, verbose_name="Father's Name")
    father_iqraa_num = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Father's Iqraa Number"
    )
    father_address = models.TextField(
        blank=True,
        null=True,
        help_text="Required if Father's Iqraa number is not provided",
        verbose_name="Father's Address"
    )
    
    # ========== MOTHER'S INFORMATION ==========
    mother_name = models.CharField(max_length=200, verbose_name="Mother's Name")
    mother_iqraa_num = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Mother's Iqraa Number"
    )
    mother_address = models.TextField(
        blank=True,
        null=True,
        help_text="Required if Mother's Iqraa number is not provided",
        verbose_name="Mother's Address"
    )
    
    # ========== SPOUSE INFORMATION ==========
    spouse_name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Spouse Name"
    )
    spouse_iqraa_num = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Spouse's Iqraa Number"
    )
    spouse_address = models.TextField(
        blank=True,
        null=True,
        help_text="Required if Spouse's Iqraa number is not provided",
        verbose_name="Spouse's Address"
    )
    
    # ========== CHILDREN INFORMATION ==========
    children = models.JSONField(
        default=list,
        blank=True,
        help_text="List of children with their details (name, age, iqraa, address)",
        verbose_name="Children"
    )
    

    
    # ========== IQRAA TENURE ==========
    tenure_from = models.DateField(verbose_name="Tenure From")
    tenure_to = models.DateField(verbose_name="Tenure To")
    iqraa_designation = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Designation at Iqraa"
    )
    iqraa_department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,  # If department is deleted, set to NULL instead of deleting alumni
        null=True,
        blank=True,
        related_name='alumni',
        verbose_name="Department at Iqraa"
    )
    iqraa_campus = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Iqraa Campus"
    )
    memorable_experience = models.TextField(
        blank=True,
        null=True,
        verbose_name="Memorable Experience at Iqraa"
    )
    
    # ========== CURRENT STATUS ==========
    current_city = models.CharField(max_length=100, verbose_name="Current City")
    professional_field = models.CharField(max_length=200, verbose_name="Professional Field")
    alumni_activities_interest = models.CharField(
        max_length=50,
        choices=ACTIVITY_INTEREST_CHOICES,
        default='Yes',
        verbose_name="Interested in Alumni Activities"
    )
    hear_about_us = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="How did you hear about us?"
    )
    
    # ========== APPROVAL WORKFLOW ==========
    hr_approved = models.BooleanField(default=False, verbose_name="HR Approved")
    conform_register = models.BooleanField(default=False, verbose_name="Confirmed Registration")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Alumni Registration"
        verbose_name_plural = "Alumni Registrations"
    
    def __str__(self):
        return f"{self.full_name}"