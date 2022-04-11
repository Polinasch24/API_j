from django.shortcuts import render

# Create your views here.
from rest_framework import status, generics
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404, ListCreateAPIView, CreateAPIView
from rest_framework.response import Response

from smart_house.models import Sensor, Measurement
from smart_house.serilizer import SensorSerializer, SensorDetailSerializer, MeasurementSerializer, \
    CreateMeasurementSerializer


class DemoView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class CreateDemoView(generics.CreateAPIView):
    serializer_class = SensorSerializer

class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class CreateMeasurement(generics.CreateAPIView):

    serializer_class = CreateMeasurementSerializer

class SensorChangeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer