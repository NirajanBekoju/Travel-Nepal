from django.shortcuts import render, Http404
from .models import Agency, Event

def agency_dashboard(request):
    if request.user.is_agency:
        agency = Agency.objects.filter(agent_id=request.user.id).first()
        context = {
            'agency':agency
        } 
        return render(request, 'agency/dashboard.html', context)
    else:
        raise Http404