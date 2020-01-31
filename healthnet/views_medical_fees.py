import logging

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from healthnet import logger, views
from healthnet.models import Account, Admission, MedicalTest, Appointment

console_logger = logging.getLogger(__name__)

def list_view(request):
    authentication_result = views.authentication_check(request, [Account.ACCOUNT_PATIENT])
    if authentication_result is not None: return authentication_result

    template_data = views.parse_session(request, {'form_button': 'Pay'})

    template_data['medtests'] = MedicalTest.objects.filter(patient=request.user, fees_paid=False)
    template_data['appointments'] = Appointment.objects.filter(patient=request.user, fees_paid=False)
    template_data['admissions'] = Admission.objects.filter(patient=request.user, fees_paid=False)
    return render(request, 'healthnet/medical_fees.html', template_data)

def pay_view(request):
    authentication_result = views.authentication_check(request, [Account.ACCOUNT_PATIENT])
    if authentication_result is not None: return authentication_result

    MedicalTest.objects.filter(patient=request.user, fees_paid=False).update(fees_paid=True)
    Appointment.objects.filter(patient=request.user, fees_paid=False).update(fees_paid=True)
    Admission.objects.filter(patient=request.user, fees_paid=False).update(fees_paid=True)

    return redirect('/profile')
