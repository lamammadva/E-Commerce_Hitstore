from celery import shared_task
from core.models import Subscriber
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from selphy.settings import EMAIL_HOST_USER
from django.conf import settings
from django.utils import timezone
from product.models import Product
from datetime import timedelta
from user.models import CustomUser

@shared_task
def send_email_to_subscribers():
    # startdate=timezone.now()
    # enddate=startdate-timedelta(days=7)
    subscriber_emails=Subscriber.objects.values_list('email',flat=True)
    most_rev=Product.objects.all()
    # (num_cons=Count{'product_review'}).order_by('-num_cons')[0:2]
    for mail in subscriber_emails:
        body=render_to_string('email_subscribers.html',context={
            'email':mail,
            'most_rev': most_rev
        })
        msg=EmailMessage(subject='Subscriber mail',body=body,
                         from_email= EMAIL_HOST_USER,
                         to=[mail,])
        msg.content_subtype ='html'
        msg.send(fail_silently=True)
    return 'completed'
                    
                        
