from django.db import models


class Services(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    @staticmethod
    def get_service_by_id(ids):
        return Services.objects.filter (id__in=ids)
    @staticmethod
    def get_all_services():
        return Services.objects.all()

