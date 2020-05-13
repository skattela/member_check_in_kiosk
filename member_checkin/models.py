from django.db import models
from django.utils import timezone


class Member(models.Model):
    first_name = models.CharField(max_length=36, blank=True, null=True)
    last_name = models.CharField(max_length=36, blank=True, null=True)
    member_id = models.CharField(max_length=36, blank=True, null=True)
    card_id = models.CharField(max_length=36, blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name + " " + self.last_name


class CheckIn(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.member.first_name + " " + self.member.last_name
