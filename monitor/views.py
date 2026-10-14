import psutil
import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from .models import SystemHealthLog

# Apna Slack Webhook URL yahan daalein
SLACK_WEBHOOK_URL = getattr(settings, 'SLACK_WEBHOOK_URL', 'YOUR_SLACK_WEBHOOK_URL_HERE')

def dashboard(request):
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    context = {
        'cpu': cpu,
        'ram': ram,
        'disk': disk,
    }
    return render(request, 'monitor/dashboard.html', context)

def system_stats_api(request):
    """JavaScript AJAX ke liye live background API"""
    cpu = psutil.cpu_percent(interval=None)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return JsonResponse({'cpu': cpu, 'ram': ram, 'disk': disk})

def health_check_view(request):
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    # Threshold limits (Agar CPU > 80% ya RAM > 85% ho)
    is_unhealthy = cpu > 80 or ram > 85 or disk > 90
    
    if is_unhealthy:
        status_message = f"WARNING: High System Load! CPU: {cpu}%, RAM: {ram}%, Disk: {disk}%"
        message_color = "danger"
    else:
        status_message = "System is healthy. No alerts needed."
        message_color = "success"
        
    # Database mein record save karein
    SystemHealthLog.objects.create(
        cpu_usage=cpu,
        ram_usage=ram,
        disk_usage=disk,
        status=status_message
    )
    
    # Slack par alert bhejne ka code
    if is_unhealthy and SLACK_WEBHOOK_URL and SLACK_WEBHOOK_URL != 'YOUR_SLACK_WEBHOOK_URL_HERE':
        payload = {"text": f"🚨 *System Alert* 🚨\n{status_message}"}
        try:
            requests.post(SLACK_WEBHOOK_URL, json=payload)
        except Exception as e:
            print("Slack error:", e)
            
    context = {
        'cpu': cpu,
        'ram': ram,
        'disk': disk,
        'status_message': status_message,
        'message_color': message_color,
    }
    return render(request, 'monitor/dashboard.html', context)