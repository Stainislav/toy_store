from django.db import models

# Information page.
class InfoPage(models.Model):

    name = models.CharField(max_length=50)
    text = models.TextField(max_length=500, blank=True, null=True, default=None)
   
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Текст"
        verbose_name_plural = "Тексты"

