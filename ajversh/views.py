from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from .models import Build, Item, Spell, Pasive, TankPasive, CategoryBuild
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
    category_list = CategoryBuild.objects.all()
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
    context = {
        'category_list': category_list,
    }
    return render(request, "user/creator.html", context)


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
    category_object = CategoryBuild.objects.get(id=category_build)
    category_validation = Build.objects.filter(category=category_object)
    name_exist = False

    for single_obj in category_validation:
        if single_obj in list(name_qs):
            name_exist = True

    if name_input == '':
        error_name = 'Wpisz nazwę buildu!'
    elif name_exist:
        error_name = 'Ta nazwa już istnieje!'
    else:
        error_name = 'none'
        if 'offhand' in body_data:
            if 'chest_pasive_tank' in body_data:
                Build.objects.create(name_build=name_input, category=category_object, role_set=body_data['role_set'], head_id=body_data['head'], chest_id=body_data['chest'],
                                    boots_id=body_data['boots'], hand_id=body_data['weapon'], off_hand_id=body_data[
                                        'offhand'], head_spell_id=body_data['head_spell'], chest_spell_id=body_data['chest_spell'],
                                    boots_spell_id=body_data['boots_spell'], weapon_spell_q_id=body_data[
                                        'weapon_spell_q'], weapon_spell_w_id=body_data['weapon_spell_w'], weapon_spell_e_id=body_data['weapon_spell_e'],
                                    head_pasive_id=body_data['head_pasive'], chest_pasive_id=body_data['chest_pasive'], chest_pasive_tank_id=body_data['chest_pasive_tank'],
                                    boots_pasive_id=body_data['boots_pasive'], weapon_pasive_id=body_data['weapon_pasive'])
            else:
                Build.objects.create(name_build=name_input, category=category_object, role_set=body_data['role_set'], head_id=body_data['head'], chest_id=body_data['chest'],
                                    boots_id=body_data['boots'], hand_id=body_data['weapon'], off_hand_id=body_data[
                                        'offhand'], head_spell_id=body_data['head_spell'], chest_spell_id=body_data['chest_spell'],
                                    boots_spell_id=body_data['boots_spell'], weapon_spell_q_id=body_data[
                                        'weapon_spell_q'], weapon_spell_w_id=body_data['weapon_spell_w'], weapon_spell_e_id=body_data['weapon_spell_e'],
                                    head_pasive_id=body_data['head_pasive'], chest_pasive_id=body_data['chest_pasive'],
                                    boots_pasive_id=body_data['boots_pasive'], weapon_pasive_id=body_data['weapon_pasive'])
        else:
            if 'chest_pasive_tank' in body_data:
                Build.objects.create(name_build=name_input, category=category_object, role_set=body_data['role_set'], head_id=body_data['head'], chest_id=body_data['chest'],
                                    boots_id=body_data['boots'], hand_id=body_data['weapon'],  head_spell_id=body_data['head_spell'], chest_spell_id=body_data['chest_spell'],
                                    boots_spell_id=body_data['boots_spell'], weapon_spell_q_id=body_data[
                                        'weapon_spell_q'], weapon_spell_w_id=body_data['weapon_spell_w'], weapon_spell_e_id=body_data['weapon_spell_e'],
                                    head_pasive_id=body_data['head_pasive'], chest_pasive_id=body_data['chest_pasive'], chest_pasive_tank_id=body_data['chest_pasive_tank'],
                                    boots_pasive_id=body_data['boots_pasive'], weapon_pasive_id=body_data['weapon_pasive'])
            else:
                Build.objects.create(name_build=name_input, category=category_object, role_set=body_data['role_set'], head_id=body_data['head'], chest_id=body_data['chest'],
                                    boots_id=body_data['boots'], hand_id=body_data['weapon'], head_spell_id=body_data['head_spell'], chest_spell_id=body_data['chest_spell'],
                                    boots_spell_id=body_data['boots_spell'], weapon_spell_q_id=body_data[
                                        'weapon_spell_q'], weapon_spell_w_id=body_data['weapon_spell_w'], weapon_spell_e_id=body_data['weapon_spell_e'],
                                    head_pasive_id=body_data['head_pasive'], chest_pasive_id=body_data['chest_pasive'],
                                    boots_pasive_id=body_data['boots_pasive'], weapon_pasive_id=body_data['weapon_pasive'])
    return JsonResponse(error_name, safe=False)


def dc_settings_view(request):
    return render(request, "user/dc-settings.html")


def profile_view(request):
    return render(request, "user/profile.html")


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
    role = qs_build.role_set
    head = qs_build.head.name
    head_img = qs_build.head.img.url
    head_spell = qs_build.head_spell.img.url
    head_spell_name = qs_build.head_spell.name
    head_pasive = qs_build.head_pasive.img.url
    head_pasive_name = qs_build.head_pasive.name

    chest = qs_build.chest.name
    chest_img = qs_build.chest.img.url
    chest_spell = qs_build.chest_spell.img.url
    chest_spell_name = qs_build.chest_spell.name
    chest_pasive = qs_build.chest_pasive.img.url
    chest_pasive_name = qs_build.chest_pasive.name

    boots = qs_build.boots.name
    boots_img = qs_build.boots.img.url
    boots_spell = qs_build.boots_spell.img.url
    boots_spell_name = qs_build.boots_spell.name
    boots_pasive = qs_build.boots_pasive.img.url
    boots_pasive_name = qs_build.boots_pasive.name

    hand = qs_build.hand.name
    hand_img = qs_build.hand.img.url
    hand_q = qs_build.weapon_spell_q.name
    hand_q_img = qs_build.weapon_spell_q.img.url
    hand_w = qs_build.weapon_spell_w.name
    hand_w_img = qs_build.weapon_spell_w.img.url
    hand_e = qs_build.weapon_spell_e.name
    hand_e_img = qs_build.weapon_spell_e.img.url
    hand_pasive = qs_build.weapon_pasive.name
    hand_pasive_img = qs_build.weapon_pasive.img.url


    modal_data = {
        'name': name,
        'role': role,
        'head': head,
        'head_img': head_img,
        'head_spell': head_spell,
        'head_spell_name': head_spell_name,
        'head_pasive': head_pasive,
        'head_pasive_name': head_pasive_name,
        'chest': chest,
        'chest_img': chest_img,
        'chest_spell': chest_spell,
        'chest_spell_name': chest_spell_name,
        'chest_pasive': chest_pasive,
        'chest_pasive_name': chest_pasive_name,
        'boots': boots,
        'boots_img': boots_img,
        'boots_spell': boots_spell,
        'boots_spell_name': boots_spell_name,
        'boots_pasive': boots_pasive,
        'boots_pasive_name': boots_pasive_name,
        'hand': hand,
        'hand_img': hand_img,
        'hand_q': hand_q,
        'hand_q_img': hand_q_img,
        'hand_w': hand_w,
        'hand_w_img': hand_w_img,
        'hand_e': hand_e,
        'hand_e_img': hand_e_img,
        'hand_pasive': hand_pasive,
        'hand_pasive_img': hand_pasive_img,
    }

    if build_filter[0].chest_pasive_tank:
        chest_pasive_tank = qs_build.chest_pasive_tank.img.url
        chest_pasive_tank_name = qs_build.chest_pasive_tank.name
        modal_data['chest_pasive_tank'] = chest_pasive_tank
        modal_data['chest_pasive_tank_name'] = chest_pasive_tank_name

    for item in build_filter:
        if item.off_hand:
            off_hand = qs_build.off_hand.name
            off_hand_img = qs_build.off_hand.img.url
            modal_data['off_hand'] = off_hand
            modal_data['off_hand_img'] = off_hand_img

    return JsonResponse(modal_data)
