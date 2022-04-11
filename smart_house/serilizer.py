from django.shortcuts import get_object_or_404
from rest_framework import serializers, request, status
from rest_framework.authtoken import models
from rest_framework.response import Response

from smart_house.models import Sensor, Measurement, Sensor_Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'


class CreateMeasurementSerializer(serializers.Serializer):

    id_sensor=Sensor.objects.all().values_list('id',flat=True)
    sensors=serializers.ChoiceField(choices=id_sensor)
    temperature=serializers.IntegerField()
    created_at=serializers.DateField()
    def create(self, validated_data):
        data=Measurement.objects.create(temperature='temperature',
                                          created_at='created_at' )
        data_1=Sensor_Measurement.objects.create(id_sensor='sensors')

        return data







class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']