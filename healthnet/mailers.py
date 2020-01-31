from datetime import datetime, timedelta

from django.core.mail import send_mail
from healthnet.models import Account, Appointment, Prescription

def send_reminder(user, event):
    if type(event) == Appointment:
        remainder_type = 'Appointment'
        body = """
        You have an upcoming appointment with {doctor} on {date} from {start_time} to {end_time}. Please contact adminstration if you are unable to make it.
        """.format(doctor=event.doctor.account.name, date=event.date, start_time=event.start_time, end_time=event.end_time)
    elif type(event) == Prescription:
        remainder_type = 'Prescription'
        body = """
        Your prescription for {medicine} is about to run out on {date}. Please refill it and contact {doctor} in case of a new prescription.
        """.format(medicine=event.medication, date=event.date + timedelta(7*event.refill), doctor=event.doctor.account.name)

    message = """
      Hi {name},
      
      {body}

      Log in into your HealthNet account for more information. Thank you for using HealthNet for all your medical needs.
    """.format(name=user.Account.name, body=body)

    send_mail(
        '[HealthNet] Remainder for '.format(remainder_type=remainder_type),
        message,
        'noreply@healthnet.com',
        [user.email],
        fail_silently=False,
    )
