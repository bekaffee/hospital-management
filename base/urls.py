from django.urls import path
from .views import PatientList, DoctorList, PatientDetail, DoctorDetail, PatientCreate, Admingo, DoctorCreate, PatientUpdate, DoctorUpdate, PatientDelete, DoctorDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', Admingo.as_view(), name='admin-page'),
    path('patients/', PatientList.as_view(), name='patients'),
    path('doctors/', DoctorList.as_view(), name='doctors'),
    path('patient/<int:pk>/', PatientDetail.as_view(), name='patient'),
    path('doctor/<int:pk>/', DoctorDetail.as_view(), name='doctor'),
    path('create-patient/', PatientCreate.as_view(), name='patient-create'),
    path('create-doctor/', DoctorCreate.as_view(), name='doctor-create'),
    path('patient-update/<int:pk>/', PatientUpdate.as_view(), name='patient-update'),
    path('doctor-update/<int:pk>/', DoctorUpdate.as_view(), name='doctor-update'),
    path('patient-delete/<int:pk>/', PatientDelete.as_view(), name='patient-delete'),
    path('doctor-delete/<int:pk>/', DoctorDelete.as_view(), name='doctor-delete'),
]