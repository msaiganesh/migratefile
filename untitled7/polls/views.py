from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
# this login required decorator is to not allow any
# view without authentication
@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")
