from django.shortcuts import render
from .forms import CreateBuildForm
from django.http import HttpResponseRedirect, JsonResponse
from .models import Build, Item
import json


def home_view(request):
    return render(request, "home.html")


def guild_view(request):
    return render(request, "user/guild.html")


def sets_creator_view(request):
    form = CreateBuildForm()
    if request.method == "POST":
        form = CreateBuildForm(request.POST)
        if form.is_valid():
            form.save()
            form = CreateBuildForm()


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


def solo_view(request):
    solo_builds = Build.objects.filter(category='Dungi Solo')
    context = {
        "solo_builds": solo_builds,
    }
    return render(request, "sets/solo.html", context)


def group_view(request):
    group_builds = Build.objects.filter(category='Dungi Grupowe')
    context = {
        "group_builds": group_builds,
    }
    return render(request, "sets/group.html", context)


def pvp_view(request):
    pvp_builds = Build.objects.filter(category='PVP')
    context = {
        "pvp_builds": pvp_builds,
    }
    return render(request, "sets/pvp.html", context)


def zvz_view(request):
    zvz_builds = Build.objects.filter(category='ZVZ')
    context = {
        "zvz_builds": zvz_builds,
    }
    return render(request, "sets/zvz.html", context)


def avalon_view(request):
    avalon_builds = Build.objects.filter(category='AVALON')
    context = {
        "avalon_builds": avalon_builds,
    }
    return render(request, "sets/avalon.html", context)


def build_info(request):
    body_data = json.loads(request.body)
    build_id = body_data['buildId']
    qs_build = Build.objects.get(id=build_id)
    build_filter = Build.objects.filter(id=build_id)
    name = qs_build.name_build
    head = qs_build.head.name
    head_t = qs_build.head_tier.tier
    head_img = qs_build.head.img.url

    chest = qs_build.chest.name
    chest_t = qs_build.chest_tier.tier
    chest_img = qs_build.chest.img.url

    boots = qs_build.boots.name
    boots_t = qs_build.boots_tier.tier
    boots_img = qs_build.boots.img.url

    hand = qs_build.hand.name
    hand_t = qs_build.hand_tier.tier
    hand_img = qs_build.hand.img.url


    modal_data = {
        'name': name,
        'head': head,
        'head_t': head_t,
        'head_img': head_img,
        'chest': chest,
        'chest_t': chest_t,
        'chest_img': chest_img,
        'boots': boots,
        'boots_t': boots_t,
        'boots_img': boots_img,
        'hand': hand,
        'hand_t': hand_t,
        'hand_img': hand_img,
    }

    for item in build_filter:
        if item.second_hand:
            second_hand = qs_build.second_hand.name
            second_hand_tier = qs_build.second_hand_tier.tier
            second_hand_img = qs_build.second_hand.img.url
            modal_data['second_hand'] = second_hand
            modal_data['second_hand_tier'] = second_hand_tier
            modal_data['second_hand_img'] = second_hand_img

    return JsonResponse(modal_data)