from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=128)
    level = models.PositiveIntegerField(default=1)

    class Meta:
        pass

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(Player,
                              null=True,
                              on_delete=models.SET_NULL)

    class Meta:
        pass

    def __str__(self):
        return self.name


class Weapon(Equipment):
    damage = models.PositiveIntegerField()

    class Meta:
        pass


class Armor(Equipment):
    defense = models.PositiveIntegerField()

    class Meta:
        pass
