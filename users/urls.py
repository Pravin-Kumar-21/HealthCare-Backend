from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.ListCreatePatientView.as_view(), name='list-create-patient'),
    path('patients/<uuid:patient_id>/', views.DetailPatientView.as_view(), name='detail-patient'),

    path('doctors/', views.ListCreateDoctorView.as_view(), name='list-create-doctor'),
    path('doctors/<uuid:doctor_id>/', views.DetailDoctorView.as_view(), name='detail-doctor'),

    path('mappings/', views.ListCreateMappingsView.as_view(), name='list-mappings'),
    path('mappings/<uuid:patient_id>/', views.PatientDoctorListView.as_view(), name='patient-doctor-list'),
    path('mappings/<uuid:mapping_id>', views.DeleteMappingView.as_view(), name='delete-mapping'),
]
