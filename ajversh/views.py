from django.shortcuts import render

def home_view(request):
    return render(request, "home.html")

def sets_list_view(request):
    return render(request, "user/sets.html")

def guild_view(request):
    return render(request, "user/guild.html")

def sets_creator_view(request):
    return render(request, "user/creator.html")

def dc_settings_view(request):
    return render(request, "user/dc-settings.html")

def profile_view(request):
    return render(request, "user/profile.html")

def edit_view(request):
    return render(request, "user/edit-profile.html")

def messages_view(request):
    return render(request, "user/messages.html")

def logout_view(request):
    pass