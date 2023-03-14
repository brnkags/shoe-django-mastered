from django.db import models


# Create your models here.
class Shoes(models.Model):
    shoename = models.CharField(max_length=100)
    shoeimage = models.URLField()
    shoeprice = models.CharField(max_length=1000000)

    class Meta:
        db_table = 'shoes'

    def __unicode__(self):
        return self.shoename

    def __str__(self):
        return self.shoename
