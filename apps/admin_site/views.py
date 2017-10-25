from django.shortcuts import render

def online_users(request):
    return render(request, 'admin/users_online.html')