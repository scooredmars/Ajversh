from django.shortcuts import render
from .forms import CreateBuildForm
from django.http import HttpResponseRedirect, JsonResponse
from .models import Build, Item
import json


def home_view(request):
    return render(request, "home.html")


def sets_list_view(request):
    all_builds = Build.objects.all()
    context = {
        "all_builds": all_builds,
    }
    return render(request, "user/sets.html", context)


def guild_view(request):
    return render(request, "user/guild.html")


def sets_creator_view(request):
    form = CreateBuildForm()
    if request.method == "POST":
        form = CreateBuildForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('sets')

    context = {
        "form": form,
    }
    return render(request, "user/creator.html", context)


def validation_weapon_form(request):
    body_data = json.loads(request.body)
    item_id = body_data['itemId']
    lock_second_hand = False

    if item_id:
        current_item = Item.objects.get(id=item_id)

        if current_item.set_part == "Broń dwuręczna":
            lock_second_hand = True

    return JsonResponse(lock_second_hand, safe=False)

def dc_settings_view(request):
    return render(request, "user/dc-settings.html")


def profile_view(request):
    return render(request, "user/profile.html")


def edit_view(request):
    return render(request, "user/edit-profile.html")


def messages_view(request):
    return render(request, "user/messages.html")
