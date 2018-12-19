from django.db import models
from django.contrib.auth.models import User


# A user of our website.
class User(User):

    phone          = models.CharField(max_length=50, blank=True, null=True, default=None)
    created        = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated        = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name        = "Пользователь"
        verbose_name_plural = "Пользователи"
  
