from django.urls import path
from . import views

urlpatterns = [
    # system monitor view to be created next
    path('monitor/', views.TrafficMonitor.as_view(), name="monitor"),
    path('update-monitor/<pk>/<ip>', views.UpdateIp.as_view(), name="update-monitor"),
    path('create-monitor/', views.CreateMonitor.as_view(), name="create-monitor"),
    path('all-monitor/', views.AllTrafficMonitor.as_view(), name="all-monitor"),

]
