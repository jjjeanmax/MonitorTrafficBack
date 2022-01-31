from django.urls import path
from . import views

urlpatterns = [
    # system monitor view to be created next
    path('monitor/', views.TrafficMonitor.as_view(), name="monitor"),
    path('monitor/<pk>', views.GetTrafficMonitorById.as_view(), name="get-traffic-monitor"),
    path('create-monitor/<ip>', views.CreateMonitorByIp.as_view(), name="create-monitor-by-id"),
    path('get-and-save-monitor/', views.GetAndSaveMonitor.as_view(), name="get-and-save-monitor"),
    path('get-all-monitor/', views.GetAllTrafficMonitor.as_view(), name="get-all-monitor"),

]
