from django.db import models

from backend.appointments.models import Appointment


class VisitRecord(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name="visit_record")
    check_in_time = models.DateTimeField("签到时间")
    check_out_time = models.DateTimeField("签退时间", null=True, blank=True)
    visitor_temperature = models.DecimalField("访客体温", max_digits=4, decimal_places=1, null=True, blank=True)
    staff_name = models.CharField("接待员工", max_length=50)
    summary = models.TextField("探视记录", blank=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        ordering = ["-check_in_time"]

    def __str__(self):
        return f"{self.appointment.family_name} {self.check_in_time:%Y-%m-%d %H:%M}"
