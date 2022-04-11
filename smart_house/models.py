from django.db import models



class Sensor(models.Model):
    name=models.CharField(max_length=60)
    description=models.CharField(max_length=100)

class Measurement(models.Model):
    sensors=models.ManyToManyField(Sensor,related_name='measurements', through='Sensor_Measurement')
    temperature = models.IntegerField()
    created_at=models.DateField()

class Sensor_Measurement(models.Model):
    measurement=models.ForeignKey(Measurement,related_name='measurements', on_delete=models.CASCADE)
    sensor=models.ForeignKey(Sensor, related_name='sensors', on_delete=models.CASCADE)