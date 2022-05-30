from django.db import models

# Create your models here.
class Symbol(models.Model):
    TICKER = models.CharField(max_length=100)
    DTYYYYMMDD = models.IntegerField(null=True , blank=True)
    FIRST = models.IntegerField(null=True , blank=True)
    HIGH = models.IntegerField(null=True , blank=True)
    LOW = models.IntegerField(null=True , blank=True)
    CLOSE = models.IntegerField(null=True , blank=True)
    VALUE = models.IntegerField(null=True , blank=True)
    VOL = models.IntegerField(null=True , blank=True)
    OPENINT = models.IntegerField(null=True , blank=True)
    PER = models.CharField(max_length=5)
    OPEN = models.IntegerField(null=True , blank=True)
    LAST = models.IntegerField(null=True , blank=True)

    def __str__(self) -> str:
        return self.TICKER