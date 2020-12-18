from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="index"),
    path("sets", views.sets_list_view, name="sets"),
    path("guild", views.guild_view, name="guild"),
    path("creator", views.sets_creator_view, name="creator"),
    path("dc-settings", views.dc_settings_view, name="dc-settings"),
    path("account", views.profile_view, name="account"),
    path("edit", views.edit_view, name="edit"),
    path("messages", views.messages_view, name="messages"),
]