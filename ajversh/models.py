from django.db import models


class Spell(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(blank=True, upload_to='spell')
    description = models.TextField()

    def __str__(self):
        return self.name


class Pasive(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(blank=True, upload_to='pasive')
    description = models.TextField()

    def __str__(self):
        return self.name


class TankPasive(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(blank=True, upload_to='pasive')
    description = models.TextField()

    def __str__(self):
        return self.name


class Item(models.Model):
    PART = (
        ('Głowa', 'Głowa'),
        ('Klata', 'Klata'),
        ('Nogi', 'Nogi'),
        ('Broń jednoręczna', 'Broń jednoręczna'),
        ('Broń dwuręczna', 'Broń dwuręczna'),
        ('Druga ręka', 'Druga ręka'),
    )
    MATERIAL = (
        ('Materiał', 'Materiał'),
        ('Skóra', 'Skóra'),
        ('Płyta', 'Płyta'),
    )
    name = models.CharField(max_length=50)
    img = models.ImageField(blank=True, upload_to='items')
    set_part = models.CharField(max_length=20, choices=PART)
    type_material = models.CharField(max_length=20, choices=MATERIAL, blank=True)
    q = models.ManyToManyField('ajversh.Spell', related_name='q_spell', blank=True)
    w = models.ManyToManyField('ajversh.Spell', related_name='w_spell', blank=True)
    e = models.ManyToManyField('ajversh.Spell', related_name='e_spell', blank=True)
    r = models.ManyToManyField('ajversh.Spell', related_name='r_spell', blank=True)
    d = models.ManyToManyField('ajversh.Spell', related_name='d_spell', blank=True)
    f = models.ManyToManyField('ajversh.Spell', related_name='f_spell', blank=True)
    pasives = models.ManyToManyField('ajversh.Pasive', related_name='pasive', blank=True)
    tank_pasives = models.ManyToManyField('ajversh.TankPasive', related_name='tank_pasive', blank=True)

    def __str__(self):
        return self.name

class CategoryBuild(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Build(models.Model):
    ROLE = (
        ('Tank', 'Tank'),
        ('Heal', 'Heal'),
        ('MDPS', 'MDPS'),
        ('RDPS', 'RDPS'),
        ('Supp', 'Supp'),
    )
    name_build = models.CharField(max_length=50)
    category = models.ForeignKey("ajversh.CategoryBuild", on_delete=models.CASCADE)
    role_set = models.CharField(max_length=20, choices=ROLE, null=True)
    head = models.ForeignKey(
        'ajversh.Item', on_delete=models.CASCADE, related_name='head_item', null=True)
    chest = models.ForeignKey(
        'ajversh.Item', on_delete=models.CASCADE, related_name='chest_item', null=True)
    boots = models.ForeignKey(
        'ajversh.Item', on_delete=models.CASCADE, related_name='boots_item', null=True)
    hand = models.ForeignKey(
        'ajversh.Item', on_delete=models.CASCADE, related_name='hand_item', null=True)
    off_hand = models.ForeignKey(
        'ajversh.Item', on_delete=models.CASCADE, related_name='off_hand_item', blank=True, null=True)

    head_spell = models.ForeignKey(
        'ajversh.Spell', on_delete=models.CASCADE, related_name='head_spell', null=True)
    chest_spell = models.ForeignKey(
        'ajversh.Spell', on_delete=models.CASCADE, related_name='chest_spell', null=True)
    boots_spell = models.ForeignKey(
        'ajversh.Spell', on_delete=models.CASCADE, related_name='boots_spell', null=True)
    weapon_spell_q = models.ForeignKey(
        'ajversh.Spell', on_delete=models.CASCADE, related_name='weapon_spell_q', null=True)
    weapon_spell_w = models.ForeignKey(
        'ajversh.Spell', on_delete=models.CASCADE, related_name='weapon_spell_w', null=True)
    weapon_spell_e = models.ForeignKey(
        'ajversh.Spell', on_delete=models.CASCADE, related_name='weapon_spell_e', null=True)

    head_pasive = models.ForeignKey(
        'ajversh.Pasive', on_delete=models.CASCADE, related_name='head_pasive', null=True)
    chest_pasive = models.ForeignKey(
        'ajversh.Pasive', on_delete=models.CASCADE, related_name='chest_pasive', null=True)
    chest_pasive_tank = models.ForeignKey(
        'ajversh.TankPasive', on_delete=models.CASCADE, related_name='chest_pasive_tank', blank=True, null=True)
    boots_pasive = models.ForeignKey(
        'ajversh.Pasive', on_delete=models.CASCADE, related_name='boots_pasive', null=True)
    weapon_pasive = models.ForeignKey(
        'ajversh.Pasive', on_delete=models.CASCADE, related_name='weapon_pasive', null=True)

    def __str__(self):
        return self.name_build
