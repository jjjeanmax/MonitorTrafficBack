from django.db import models


class Monitor(models.Model):
    continent = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    capital = models.CharField(max_length=50, blank=True, null=True)
    datetime = models.DateField(max_length=50, blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = "Monitor"
        verbose_name_plural = "Monitors"
