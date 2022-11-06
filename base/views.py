from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Patient, Doctor, Admingo


class PatientList(LoginRequiredMixin, ListView):
    model = Patient
    context_object_name = 'patients'
    template_name = 'base/patient_list.html'


class DoctorList(LoginRequiredMixin, ListView):
    model = Doctor
    context_object_name = 'doctors'
    template_name = 'base/doctor_list.html'


class PatientDetail(LoginRequiredMixin, DetailView):
    model = Patient
    context_object_name = 'patient'
    template_name = 'base/patient_detail.html'


class DoctorDetail(LoginRequiredMixin, DetailView):
    model = Doctor
    context_object_name = 'doctor'
    template_name = 'base/doctor_detail.html'


class PatientCreate(LoginRequiredMixin, CreateView):
    model = Patient
    fields = [
        'date_of_birth', 'iin_number', 'id_number', 'name_surname_middlename',
        'blood_group', 'emergency_contact_number', 'contact_number', 'email',
        'address', 'martial_status', 'registration_date', 'other_details'
    ]
    success_url = reverse_lazy('patients')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PatientCreate, self).form_valid(form)


class DoctorCreate(LoginRequiredMixin, CreateView):
    model = Doctor
    fields = [
        'date_of_birth', 'iin_number', 'id_number', 'name_surname_middlename', 
        'contact_number', 'department_id', 'specialization_details_id', 
        'experience_in_years', 'photo_of_the_doctor', 'category', 
        'price_of_the_appointment', 'schedule_details', 
        'degree_or_education', 'rating', 'address', 'homepage_url'
    ]
    success_url = reverse_lazy('doctors')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DoctorCreate, self).form_valid(form)


class Admingo(LoginRequiredMixin, ListView):
    model = Admingo
    context_object_name = 'admingo'
    template_name = 'base/admin_page.html'


class PatientUpdate(LoginRequiredMixin, UpdateView):
    model = Patient
    fields = [
        'date_of_birth', 'iin_number', 'id_number', 'name_surname_middlename',
        'blood_group', 'emergency_contact_number', 'contact_number', 'email',
        'address', 'martial_status', 'registration_date', 'other_details'
    ]
    success_url = reverse_lazy('patients')


class DoctorUpdate(LoginRequiredMixin, UpdateView):
    model = Doctor
    fields = [
        'date_of_birth', 'iin_number', 'id_number', 'name_surname_middlename', 
        'contact_number', 'department_id', 'specialization_details_id', 
        'experience_in_years', 'photo_of_the_doctor', 'category', 
        'price_of_the_appointment', 'schedule_details', 
        'degree_or_education', 'rating', 'address', 'homepage_url'
    ]
    success_url = reverse_lazy('doctors')


class PatientDelete(LoginRequiredMixin, DeleteView):
    model = Patient
    context_object_name = 'patient'
    success_url = reverse_lazy('patients')


class DoctorDelete(LoginRequiredMixin, DeleteView):
    model = Doctor
    context_object_name = 'doctor'
    success_url = reverse_lazy('doctors')


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('admin-page')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('admin-page')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('admin-page')
        return super(RegisterPage, self).get(*args, **kwargs)