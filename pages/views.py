from django.shortcuts import render
from explore.models import Inquiry

# Create your views here.
def index(request):
    return render(request, "pages/index.html")

def user_dashboard(request):
    inquiries = Inquiry.objects.filter(user_id=request.user).order_by('-registered_date')
    context = {
        'inquiries':inquiries
    }
    return render(request, "pages/user_dashboard.html", context)