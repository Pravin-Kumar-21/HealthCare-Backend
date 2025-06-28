from django.contrib import admin
from .models import Patient, Doctor, PatientDoctorMapping

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'gender', 'age']
    search_fields = ['first_name', 'last_name', 'email']
    filter_horizontal = ['doctors']  

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['full_name_and_details', 'email', 'specialization', 'experience']
    search_fields = ['first_name', 'last_name', 'email']


@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):  
    list_display = ['mapping_id', 'patient_id', 'doctor_id', 'created_at']
    search_fields = ['patient_id__first_name', 'doctor_id__first_name']
    list_filter = ['created_at']