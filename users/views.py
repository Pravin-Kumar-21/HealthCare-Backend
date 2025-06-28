from django.shortcuts import get_object_or_404
from users.models import Patient, Doctor, PatientDoctorMapping
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.serializers import PatientSerializer, DoctorSerializer, PatientDoctorMappingSerializer


class ListCreatePatientView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]


class DetailPatientView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'patient_id'

class ListCreateDoctorView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]


class DetailDoctorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'doctor_id'


class ListCreateMappingsView(generics.ListCreateAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [AllowAny]


class PatientDoctorListView(generics.ListAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return PatientDoctorMapping.objects.filter(patient_id__patient_id=patient_id)


class DeleteMappingView(generics.DestroyAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [AllowAny]
    lookup_field = 'mapping_id'
