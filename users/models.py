from django.db import models
import uuid

class Patient(models.Model):
  
    gender_choices = [
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]

    patient_id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=100, verbose_name="First Name", blank=False)
    last_name = models.CharField(max_length=100, verbose_name="Last Name", blank=False)
    email = models.EmailField(unique=True, verbose_name="Email", blank=False)
    gender = models.CharField(max_length=10, choices=gender_choices, verbose_name="Gender", blank=False)
    age = models.PositiveIntegerField(verbose_name="Age", blank=False)
    phone_number = models.CharField(max_length=10, verbose_name="Phone Number", blank=False)
    date_of_birth = models.DateField(verbose_name="Date of Birth", blank=False)
    doctors = models.ManyToManyField('Doctor', related_name='patients')
    address = models.TextField(verbose_name="Address", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
      
      
class Doctor(models.Model):
    doctor_id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True) 
    first_name = models.CharField(max_length=100, verbose_name="First Name", blank=False)
    last_name = models.CharField(max_length=100, verbose_name="Last Name", blank=False)
    email = models.EmailField(unique=True, verbose_name="Email", blank=False)
    phone_number = models.CharField(max_length=10, verbose_name="Phone Number", blank=False)
    specialization = models.CharField(max_length=100, verbose_name="Specialization", blank=False)
    experience = models.PositiveIntegerField(verbose_name="Years of Experience", blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def full_name_and_details(self):
        return f"{self.doctor_id}   ->   {self.first_name} {self.last_name}    ->   {self.specialization} "

    def __str__(self):
        return self.full_name_and_details()



class PatientDoctorMapping(models.Model):
    mapping_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="doctor_mappings" , to_field='patient_id')
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="patient_mappings" , to_field='doctor_id')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('patient_id', 'doctor_id')  

    def __str__(self):
        return f"{self.patient_id.full_name()} <-> {self.doctor_id.full_name()}"
