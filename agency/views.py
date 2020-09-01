from django.shortcuts import render, Http404, HttpResponse, get_object_or_404, redirect
from .models import Agency, Event
from django.contrib import messages
from .forms import AddEventForm, UpdateEventForm
from .decorators import is_agency

@is_agency
def agency_dashboard(request):
    agency = Agency.objects.filter(agent_id=request.user.id).first()
    upcoming_events = Event.objects.filter(is_display=True, agency_id=request.user.agency)
    recent_events = Event.objects.filter(is_display=False, agency_id=request.user.agency).order_by('-updated_date')[:10]

    context = {
        'agency':agency,
        'upcoming_events':upcoming_events,
        'recent_events':recent_events
    } 
    return render(request, 'agency/dashboard.html', context)
    
# CRUD OPERATION FOR EVENTS
@is_agency
def add_event(request):
    # Access if and only if user is agency 
    if request.method == 'POST':
        form = AddEventForm(request.POST, request.FILES)
        if form.is_valid():
            addEvent = form.save(commit=False)
            addEvent.agency_id = request.user.agency
            add_event = addEvent.save()
            messages.success(request, 'Event has been added successfully.')
            return redirect('agency_dashboard')
        else:
            context = {
                'form':form
            }
            return render(request, 'agency/add_event.html', context)
    else:
        form = AddEventForm()
        context = {
            'form':form
        }
        return render(request, 'agency/add_event.html', context)

@is_agency
def show_event(request, id):
    event = Event.objects.filter(id = id).first()
    # check if the event belongs to the agency
    if event.agency_id != request.user.agency:
        raise Http404
  
    context = {
        'event':event
    }
    return render(request, 'agency/show_event.html', context)

@is_agency
def update_event(request, id):
    event = get_object_or_404(Event, id=id)
    form = AddEventForm(request.POST or None, instance= event)

    if request.method == "POST":
        form = UpdateEventForm(request.POST or None, request.FILES or None, instance=event)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request, 'Event has been updated successfully')
            return redirect('agency_dashboard')

        else:
            context = {
                'form':form
            }
            return render(request, 'agency/edit_event.html')
    
    else:
        form = UpdateEventForm(
            initial={
                'title':event.title,
                'description':event.description,
                'image':event.image,
                'location':event.location,
                'booking_date_limit':event.booking_date_limit
            }
        )
        context = {
            'form':form,
            'id':id
        }
        return render(request, 'agency/edit_event.html', context)

@is_agency
def delete_event(request, id):
    if request.method == "POST":
        event = Event.objects.filter(id=id).first()
        if event.agency_id == request.user.agency:
            event.is_display = False
            event.save()
            messages.success(request, 'Event has been hided successfully.')
            return redirect('agency_dashboard')
        else:
            messages.error(request, 'You are not authorized to delete this event.')
            return redirect('agency_dashboard')
    