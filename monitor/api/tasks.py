from django.utils import timezone

from celery import shared_task

from .models import Monitor


@shared_task
def delete_undefined_data():
    """
    delete every 5 minutes undefined city or country or capital
    :return: str
    """
    monitors = Monitor.objects.all()
    for monitor in monitors:
        if monitor.city is None or monitor.capital is None or monitor.country is None or monitor.continent is None:
            monitor.delete()
    return "completed deleting monitors at {}".format(timezone.now())
