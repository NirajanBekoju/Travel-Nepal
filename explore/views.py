from django.shortcuts import render, redirect
from django.http import Http404
from agency.models import Event
from .models import Inquiry
from django.contrib import messages


# Create your views here.
def explore(request):
    events = Event.objects.filter(is_display=True).order_by('-registered_date')
    context = {
        'events':events
    }
    return render(request, 'explore/explore.html', context)

def explore_event(request, id):
    event = Event.objects.filter(is_display=True, id=id).first()
    if event:
        context = {
            'event':event
        }
        return render(request, 'explore/explore_event.html', context)
    else:
        raise Http404

def event_inquiry(request, id):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        phone = request.POST["phone"]    
        user_id = request.user
        event_id = Event.objects.filter(id=id).first()
        # Check if the user has alread made an inquiry
        if request.user.is_authenticated:
            user_id = request.user
            has_inquired = Inquiry.objects.filter(event_id=event_id, user_id=user_id).first()
            if has_inquired:
                messages.error(request, "You have already made an inquiry for this event.")
                return redirect('explore')
        
        inquiry = Inquiry(first_name = first_name, last_name=last_name, email=email, phone=phone, event_id=event_id, user_id=user_id)
        inquiry.save()
        messages.success(request, "Inquiry has been sent successfully...")
        return redirect('explore')

