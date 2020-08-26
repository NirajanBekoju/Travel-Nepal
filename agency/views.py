from django.shortcuts import render, Http404

def agency_dashboard(request):
    if request.user.is_agency:
        return render(request, 'agency/dashboard.html')
    else:
        raise Http404