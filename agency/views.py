from django.shortcuts import render, Http404, HttpResponse
from .models import Agency, Event

from .forms import AddEventForm

def agency_dashboard(request):
    if request.user.is_agency:
        agency = Agency.objects.filter(agent_id=request.user.id).first()
        context = {
            'agency':agency
        } 
        return render(request, 'agency/dashboard.html', context)
    else:
        raise Http404

# CRUD OPERATION FOR EVENTS
def add_event(request):
    # Access if and only if user is agency 
    if request.user.is_agency:
        if request.method == 'POST':
            form = AddEventForm(request.POST, request.FILES)
            if form.is_valid():
                addEvent = form.save(commit=False)
                addEvent.agency_id = request.user.agency
                add_event = addEvent.save()
                print('======================================')
                print(add_event)
                print('======================================')
                return HttpResponse('Form Saved')
            else:
                print('======================================')
                print(form.errors)
                print('======================================')
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