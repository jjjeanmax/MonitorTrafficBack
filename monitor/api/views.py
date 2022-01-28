from django.shortcuts import render, redirect
import requests
import datetime
import psutil
import os
from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Monitor
from .serializers import AllMonitorSerializers
from django.core.paginator import Paginator
from monitor.settings.base import access_key, API_URL


# traffic monitor
class TrafficMonitor(APIView):
    "pagination inutile"

    @staticmethod
    def get(request):
        dataSaved = Monitor.objects.all().order_by('-datetime')
        # Getting loadover15 minutes
        load1, load5, load15 = psutil.getloadavg()
        cpu_usage = int((load15 / os.cpu_count()) * 100)
        ram_usage = int(psutil.virtual_memory()[2])
        p = Paginator(dataSaved, 100)
        # shows number of items in page
        totalSiteVisits = p.count
        # find unique page viewers & Duration
        pageNum = request.GET.get('page', 1)
        page1 = p.page(pageNum)
        # unique page viewers
        a = Monitor.objects.order_by().values('ip').distinct()
        pp = Paginator(list(a), 10)
        # shows number of items in page
        unique = pp.count
        # update time
        now = datetime.now()
        data = {
            "now": now,
            "unique": unique,
            "totalSiteVisits": totalSiteVisits,
            "cpu_usage": cpu_usage,
            "ram_usage": ram_usage,
            "dataSaved": str(page1),
        }
        if data:
            # # Проверка соответствия формата данных
            # serializer.is_valid(raise_exception=True)

            return Response(status=status.HTTP_200_OK, data=data)


class CreateMonitor(APIView):
    @staticmethod
    def post(request):
        print(request.META.get('ip'))
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        # change from HTTP to HTTPS on the IPSTACK API if you have a premium account
        response = requests.get(f'{API_URL}' + f'{ip}' + f'?access_key={access_key}')
        rawData = response.json()
        print(rawData)  # print this out to look at the response
        continent = rawData['continent_name']
        country = rawData['country_name']
        city = rawData['city']
        capital = rawData['location']['capital']
        now = datetime.now()
        # datetimenow = now.strftime("%Y-%M-%D %H:%M:%S")
        saveNow = Monitor(
            continent=continent,
            country=country,
            capital=capital,
            city=city,
            datetime=now,
            ip=ip
        )
        saveNow.save()
        data = {"ip": ip, "continent": continent, "country": country, "city": city, "capital": capital, "now": now}
        return Response(status=status.HTTP_201_CREATED, data=data)


class UpdateIp(APIView):
    @staticmethod
    def put(request, pk, ip):
        try:
            qs = Monitor.objects.get(id=pk)
        except Monitor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        response = requests.get(f'{API_URL}' + f'{ip}' + f'?access_key={access_key}')
        rawData = response.json()
        continent = rawData['continent_name']
        country = rawData['country_name']
        city = rawData['city']
        capital = rawData['location']['capital']
        now = datetime.now()
        # datetimenow = now.strftime("%Y-%M-%D %H:%M:%S")
        saveNow = Monitor(
            continent=continent,
            country=country,
            capital=capital,
            city=city,
            datetime=now,
            ip=ip
        )
        saveNow.save()
        data = {"ip": ip, "continent": continent, "country": country, "city": city, "capital": capital, "now": now}
        return Response(status=status.HTTP_200_OK, data=data)


class AllTrafficMonitor(APIView):
    @staticmethod
    def get(request):
        data = Monitor.objects.all().order_by('-datetime')
        # for dt in data:
        #     data = {
        #         "ip": dt.ip,
        #         "continent": dt.continent,
        #         "country": dt.country,
        #         "city": dt.city,
        #         "capital": dt.capital,
        #         "datetime": dt.datetime
        #     }
        # print(data)

        serializer = AllMonitorSerializers(data, many=True)
        return Response(serializer.data)
