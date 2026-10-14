from django.db import models

class SystemHealthLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    cpu_usage = models.FloatField()
    ram_usage = models.FloatField()
    disk_usage = models.FloatField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.timestamp} - CPU: {self.cpu_usage}% | RAM: {self.ram_usage}%"