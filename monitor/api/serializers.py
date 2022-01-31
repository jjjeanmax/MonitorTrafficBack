from rest_framework import serializers

from .models import Monitor
from .shemas import monitor_serializer_schema


class MonitorSerializers(serializers.Serializer):
    "inutile"

    now = serializers.DateTimeField(required=True)
    unique = serializers.IntegerField(required=True)
    totalSiteVisits = serializers.IntegerField(required=True)
    cpu_usage = serializers.IntegerField(required=True)
    ram_usage = serializers.IntegerField(required=True)
    dataSaved = serializers.CharField(required=True)

    class Meta:
        swagger_schema_fields = monitor_serializer_schema


class SaveMonitorSerializers(serializers.Serializer):
    "inutile"

    def create(self, validated_data):
        return Monitor.objects.create(**validated_data)

    class Meta:
        model = Monitor


class AllMonitorSerializers(serializers.Serializer):
    datetime = serializers.DateField(required=True)
    ip = serializers.CharField(required=True)
    capital = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    continent = serializers.CharField(required=True)

    class Meta:
        model = Monitor
