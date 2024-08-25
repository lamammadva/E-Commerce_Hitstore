from core.form import  SubscriberForm


# def get_subscriber_form(request):
#     subscriber_form=SubscriberForm()
#     if request.method == "POST":
#         subscriber_form=SubscriberForm(request.POST)
#         if subscriber_form.is_valid():
#             subscriber_form.save()
#     else:
#         subscriber_form=SubscriberForm()
#     return {'subscribe_form' : subscriber_form}

def get_subscriber_form(request):
    if request.method == "POST" and 'subscriber' in request.POST:
        subscriber_form = SubscriberForm(request.POST)
        if subscriber_form.is_valid():
            subscriber_form.save()
    else:
        subscriber_form = SubscriberForm()

    return {'subscriber_form': subscriber_form}

