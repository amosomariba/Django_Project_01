from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
