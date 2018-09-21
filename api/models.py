from django.db import models


class Roles(models.Model):
    roles = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.roles


class Users(models.Model):
    username = models.CharField(max_length=20)
    roles = models.ManyToManyField(Roles)

    def __str__(self):
        return self.username
