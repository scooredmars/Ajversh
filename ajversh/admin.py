from django.contrib import admin

from .models import Spell, Pasive, Tier, Item, Build

admin.site.register(Tier)

@admin.register(Spell)
class SpellAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
    )
    search_fields = ["name"]


@admin.register(Pasive)
class PasiveAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
    )
    search_fields = ["name"]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "set_part",
    )
    list_filter = ("set_part",)
    search_fields = ["name"]


@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    list_display = (
        "name_build",
        "category",
        "head",
        "chest",
        "boots",
        "hand",
        "off_hand",
    )
    list_filter = ("category",)
    search_fields = ["name_build"]
