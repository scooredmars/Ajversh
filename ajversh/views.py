from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from .models import Build, Item, Spell, Pasive, TankPasive
import json
from django.core import serializers
from itertools import chain


def home_view(request):
    return render(request, "home.html")


def guild_view(request):
    return render(request, "user/guild.html")


def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]


def sets_creator_view(request):
    if request.body:
        body_data = json.loads(request.body)
        item_id = body_data['type']
        if item_id == 'head':
            items_json = ValuesQuerySetToDict(Item.objects.filter(
                set_part='Głowa').values('name', 'img', 'pk'))
        elif item_id == 'chest':
            items_json = ValuesQuerySetToDict(Item.objects.filter(
                set_part='Klata').values('name', 'img', 'pk'))
        elif item_id == 'boots':
            items_json = ValuesQuerySetToDict(Item.objects.filter(
                set_part='Nogi').values('name', 'img', 'pk'))
        elif item_id == 'weapon':
            items_json = ValuesQuerySetToDict(Item.objects.filter(
                set_part__in=['Broń jednoręczna', 'Broń dwuręczna']).values('name', 'img', 'pk'))
        elif item_id == 'offhand':
            items_json = ValuesQuerySetToDict(Item.objects.filter(
                set_part='Druga ręka').values('name', 'img', 'pk'))
        return HttpResponse(json.dumps(items_json), content_type='application/javascript; charset=utf8')
    return render(request, "user/creator.html")


def item_spells(request):
    body_data = json.loads(request.body)
    item_type = body_data['type']
    item_id = body_data['pk']
    item_category = body_data['category']

    if item_category == 'pasive':
        qs = Item.objects.get(id=item_id)
        spells = ValuesQuerySetToDict(Pasive.objects.filter(
            pasive__in=[item_id]).values('id', 'name', 'img', 'description'))
        if (qs.set_part == 'Klata') and (qs.type_material == 'Płyta'):
            spells.append({'tank_item': 'True'})
        if qs.set_part == 'Broń dwuręczna':
            spells.append({'lock_offhand': 'True'})
        else:
            spells.append({'lock_offhand': 'False'})
    elif item_category == 'tankPasive':
        spells = ValuesQuerySetToDict(TankPasive.objects.filter(
            tank_pasive__in=[item_id]).values('id', 'name', 'img', 'description'))

    if item_type == 'head':
        if item_category == 'spell':
            spells = ValuesQuerySetToDict(Spell.objects.filter(
                d_spell__in=[item_id]).values('id', 'name', 'img', 'description'))
    elif item_type == 'chest':
        if item_category == 'spell':
            spells = ValuesQuerySetToDict(Spell.objects.filter(
                r_spell__in=[item_id]).values('id', 'name', 'img', 'description'))
    elif item_type == 'boots':
        if item_category == 'spell':
            spells = ValuesQuerySetToDict(Spell.objects.filter(
                f_spell__in=[item_id]).values('id', 'name', 'img', 'description'))
    elif (item_type == 'weapon') and (item_category == 'spell'):
        function_loop = int(body_data['loop'])
        if function_loop == 1:
            spells = ValuesQuerySetToDict(Spell.objects.filter(
                q_spell__in=[item_id]).values('id', 'name', 'img', 'description'))
        elif function_loop == 2:
            spells = ValuesQuerySetToDict(Spell.objects.filter(
                w_spell__in=[item_id]).values('id', 'name', 'img', 'description'))
        elif function_loop == 21:
            spells = ValuesQuerySetToDict(Spell.objects.filter(
                e_spell__in=[item_id]).values('id', 'name', 'img', 'description'))

    return HttpResponse(json.dumps(spells), content_type='application/javascript; charset=utf8')


def save_view(request):
    body_data = json.loads(request.body)
    name_input = body_data['inputVal']
    category_build = body_data['category']
    name_qs = Build.objects.filter(name_build=name_input)
    category_check = Build.objects.filter(category=category_build)
    name_exist = False

    for single_obj in category_check:
        if single_obj in list(name_qs):
            name_exist = True

    try:
        if not name_input:
            error_name = 'Wpisz nazwę buildu!'
        else:
            if name_exist:
                error_name = 'Ta nazwa już istnieje!'
            else:
                error_name = 'none'
                if body_data['offhand']:
                    Build.objects.create(name_build=name_input, category=category_build, role_set=body_data['role_set'], head_id=body_data['head'], chest_id=body_data['chest'],
                                         boots_id=body_data['boots'], hand_id=body_data['weapon'], off_hand_id=body_data[
                                             'offhand'], head_spell_id=body_data['head_spell'], chest_spell_id=body_data['chest_spell'],
                                         boots_spell_id=body_data['boots_spell'], weapon_spell_q_id=body_data[
                                             'weapon_spell_q'], weapon_spell_w_id=body_data['weapon_spell_w'], weapon_spell_e_id=body_data['weapon_spell_e'],
                                         head_pasive_id=body_data['head_pasive'], chest_pasive_id=body_data['chest_pasive'], chest_pasive_tank_id=body_data['chest_pasive_tank'], boots_pasive_id=body_data['boots_pasive'], weapon_pasive_id=body_data['weapon_pasive'])
    except KeyError:
        if not name_input:
            error_name = 'Wpisz nazwę buildu!'
        else:
            if name_exist:
                error_name = 'Ta nazwa już istnieje!'
            else:
                error_name = 'none'
                Build.objects.create(name_build=name_input, category=category_build, role_set=body_data['role_set'], head_id=body_data['head'], chest_id=body_data['chest'],
                                     boots_id=body_data['boots'], hand_id=body_data['weapon'], head_spell_id=body_data[
                                         'head_spell'], chest_spell_id=body_data['chest_spell'], boots_spell_id=body_data['boots_spell'],
                                     weapon_spell_q_id=body_data['weapon_spell_q'], weapon_spell_w_id=body_data[
                                         'weapon_spell_w'], weapon_spell_e_id=body_data['weapon_spell_e'],
                                     head_pasive_id=body_data['head_pasive'], chest_pasive_id=body_data['chest_pasive'], chest_pasive_tank_id=body_data['chest_pasive_tank'], boots_pasive_id=body_data['boots_pasive'], weapon_pasive_id=body_data['weapon_pasive'])
    return JsonResponse(error_name, safe=False)


def dc_settings_view(request):
    return render(request, "user/dc-settings.html")


def profile_view(request):
    return render(request, "user/profile.html")


def edit_view(request):
    return render(request, "user/edit-profile.html")


def messages_view(request):
    return render(request, "user/messages.html")


def solo_view(request):
    solo_builds = Build.objects.filter(category='Solo Dungi')
    context = {
        "solo_builds": solo_builds,
    }
    return render(request, "sets/solo.html", context)


def group_view(request):
    group_builds = Build.objects.filter(category='Grupowe Dungi')
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
    head_img = qs_build.head.img.url

    chest = qs_build.chest.name
    chest_img = qs_build.chest.img.url

    boots = qs_build.boots.name
    boots_img = qs_build.boots.img.url

    hand = qs_build.hand.name
    hand_img = qs_build.hand.img.url

    modal_data = {
        'name': name,
        'head': head,
        'head_img': head_img,
        'chest': chest,
        'chest_img': chest_img,
        'boots': boots,
        'boots_img': boots_img,
        'hand': hand,
        'hand_img': hand_img,
    }

    for item in build_filter:
        if item.off_hand:
            off_hand = qs_build.off_hand.name
            off_hand_img = qs_build.off_hand.img.url
            modal_data['off_hand'] = off_hand
            modal_data['off_hand_img'] = off_hand_img

    return JsonResponse(modal_data)
