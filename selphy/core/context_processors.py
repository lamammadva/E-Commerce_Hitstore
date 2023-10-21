from .form import  SubscriberForm


def get_subscriber_form(request):
    subscriber_form=SubscriberForm()
    if request.method=="POST":
        subscriber_form=SubscriberForm(request.POST)
        if subscriber_form.is_valid():
            subscriber_form.save()
    else:
        subscriber_form=SubscriberForm()
    return {'subscribe_form' : subscriber_form}



