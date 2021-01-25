from django import forms
from .models import Build, Item
from django.core.exceptions import ValidationError
from django.db import models


class CreateBuildForm(forms.ModelForm):
    class Meta:
        model = Build
        fields = ('name_build', 'category', 'head', 'head_tier', 'chest', 'chest_tier',
                  'boots', 'boots_tier', 'hand', 'hand_tier', 'second_hand', 'second_hand_tier')
    head_spells = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super(CreateBuildForm, self).__init__(*args, **kwargs)
        self.fields['head'].queryset = Item.objects.filter(set_part='Głowa')
        self.fields['chest'].queryset = Item.objects.filter(set_part='Klata')
        self.fields['boots'].queryset = Item.objects.filter(set_part='Nogi')
        self.fields['hand'].queryset = Item.objects.filter(
            set_part__in=['Broń jednoręczna', 'Broń dwuręczna'])
        self.fields['second_hand'].queryset = Item.objects.filter(
            set_part='Druga broń')

        self.fields["category"].widget.attrs.update({"class": "select-build"})
        self.fields["head"].widget.attrs.update({"class": "select-build"})
        self.fields["chest"].widget.attrs.update({"class": "select-build"})
        self.fields["boots"].widget.attrs.update({"class": "select-build"})
        self.fields["hand"].widget.attrs.update({"class": "select-build"})
        self.fields["second_hand"].widget.attrs.update(
            {"class": "select-build"})

    def clean(self, *args, **keyargs):
        name_build = self.cleaned_data.get("name_build")
        exists_build = Build.objects.filter(name_build=name_build)
        if exists_build:
            raise ValidationError("Bierząca nazwa buildu już istnieje!")
        return super(CreateBuildForm, self).clean(*args, **keyargs)
