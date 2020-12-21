from django.db import models


class Spell(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Pasive(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Tier(models.Model):
    NUMBER = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('4.1', '4.1'),
        ('4.2', '4.2'),
        ('4.3', '4.3'),
        ('5.1', '5.1'),
        ('5.2', '5.2'),
        ('5.3', '5.3'),
        ('6.1', '6.1'),
        ('6.2', '6.2'),
        ('6.3', '6.3'),
        ('7.1', '7.1'),
        ('7.2', '7.2'),
        ('7.3', '7.3'),
        ('8.1', '8.1'),
        ('8.2', '8.2'),
        ('8.3', '8.3'),
    )
    tier = models.CharField(choices=NUMBER, max_length=5)

    def __str__(self):
        return self.tier


class Item(models.Model):
    PART = (
        ('Głowa', 'Głowa'),
        ('Klata', 'Klata'),
        ('Nogi', 'Nogi'),
        ('Broń jednoręczna', 'Broń jednoręczna'),
        ('Broń dwuręczna', 'Broń dwuręczna'),
        ('Druga broń', 'Druga broń'),
    )
    name = models.CharField(max_length=50)
    img = models.ImageField(blank=True)
    spells = models.ManyToManyField('ajversh.Spell')
    pasives = models.ManyToManyField('ajversh.Pasive')
    set_part = models.CharField(max_length=20, choices=PART)

    def __str__(self):
        return self.name


class Build(models.Model):
    NAME = (
        ('Dungi Grupowe', 'Dungi Grupowe'),
        ('Dungi Solo', 'Dungi Solo'),
        ('PVP', 'PVP'),
        ('ZVZ', 'ZVZ'),
        ('AVALON', 'AVALON'),
    )
    name_build = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=NAME, null=True)
    head = models.OneToOneField(
        'ajversh.Item', on_delete=models.CASCADE, related_name='head_item', null=True)
    head_tier = models.OneToOneField(
        'ajversh.Tier', on_delete=models.CASCADE, related_name='head_tier', null=True)

    chest = models.OneToOneField(
        'ajversh.Item', on_delete=models.CASCADE, related_name='chest_item', null=True)
    chest_tier = models.OneToOneField(
        'ajversh.Tier', on_delete=models.CASCADE, related_name='chest_tier', null=True)

    boots = models.OneToOneField(
        'ajversh.Item', on_delete=models.CASCADE, related_name='boots_item', null=True)
    boots_tier = models.OneToOneField(
        'ajversh.Tier', on_delete=models.CASCADE, related_name='boots_tier', null=True)

    hand = models.OneToOneField(
        'ajversh.Item', on_delete=models.CASCADE, related_name='hand_item', null=True)
    hand_tier = models.OneToOneField(
        'ajversh.Tier', on_delete=models.CASCADE, related_name='hand_tier', null=True)

    second_hand = models.OneToOneField(
        'ajversh.Item', on_delete=models.CASCADE, related_name='second_hand_item', blank=True, null=True)
    second_hand_tier = models.OneToOneField(
        'ajversh.Tier', on_delete=models.CASCADE, related_name='second_hand_tier', blank=True, null=True)

    def __str__(self):
        return self.name_build
