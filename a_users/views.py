from django.shortcuts import render

# Create your views here.

def profile_view(request):
    profile = request.user.profile
    return render(request, 'a_users/profile.html', {'profile': profile})