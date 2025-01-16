from django.db import models

class CarModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'car'
        verbose_name_plural = 'cars'



class DateModel(models.Model):
    date = models.DateField()
    price = models.IntegerField()
    def __str__(self):
        return str(self.price)


    class Meta:
        verbose_name = 'date'
        verbose_name_plural = 'dates'


class TextModel(models.Model):
    text = models.CharField(max_length=255)
    time = models.DateField()
    quantity = models.IntegerField()
    def __str__(self):
        return self.text


    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
