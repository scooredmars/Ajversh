from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="index"),
    path("solo", views.solo_view, name="solo"),
    path("group", views.group_view, name="group"),
    path("pvp", views.pvp_view, name="pvp"),
    path("zvz", views.zvz_view, name="zvz"),
    path("avalon", views.avalon_view, name="avalon"),
    path("build-info", views.build_info, name="build-info"),
    path("guild", views.guild_view, name="guild"),
    path("creator", views.sets_creator_view, name="creator"),
    path("form-change", views.validation_weapon_form, name="form-change"),
    path("dc-settings", views.dc_settings_view, name="dc-settings"),
    path("account", views.profile_view, name="account"),
    path("edit", views.edit_view, name="edit"),
    path("messages", views.messages_view, name="messages"),
]
