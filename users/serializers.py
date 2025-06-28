from rest_framework import serializers
from .models import Patient, Doctor, PatientDoctorMapping

# Doctor Serializer
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


# Patient Serializer
class PatientSerializer(serializers.ModelSerializer):
    doctors = DoctorSerializer(many=True, read_only=True)  
    doctor_ids = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.all(),
        many=True,
        write_only=True,
        source='doctors',
        pk_field=serializers.UUIDField()
    )


    class Meta:
        model = Patient
        fields = [
            'patient_id',
            'first_name',
            'last_name',
            'email',
            'gender',
            'age',
            'phone_number',
            'date_of_birth',
            'address',
            'created_at',
            'updated_at',
            'doctors',      
            'doctor_ids',   
        ]
        
    def create(self, validated_data):
        doctors = validated_data.pop('doctors', [])
        patient = Patient.objects.create(**validated_data)
        patient.doctors.set(doctors)

        for doctor in doctors:
            PatientDoctorMapping.objects.create(patient=patient, doctor=doctor)

        return patient



class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient_id.full_name', read_only=True)
    doctor_name = serializers.CharField(source='doctor_id.full_name', read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ['mapping_id', 'patient_id', 'doctor_id', 'patient_name', 'doctor_name', 'created_at']
