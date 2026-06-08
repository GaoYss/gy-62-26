from django.db import models

from backend.residents.models import Resident


class Appointment(models.Model):
    STATUS_CHOICES = [
        ("pending", "待审核"),
        ("approved", "已通过"),
        ("rejected", "已拒绝"),
        ("completed", "已完成"),
        ("cancelled", "已取消"),
    ]

    resident = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name="appointments")
    family_name = models.CharField("家属姓名", max_length=50)
    family_phone = models.CharField("家属电话", max_length=30)
    relationship = models.CharField("关系", max_length=30)
    visit_time = models.DateTimeField("预约探视时间")
    visitor_count = models.PositiveIntegerField("访客人数", default=1)
    status = models.CharField("状态", max_length=20, choices=STATUS_CHOICES, default="pending")
    notes = models.TextField("备注", blank=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        ordering = ["-visit_time"]

    def __str__(self):
        return f"{self.family_name} -> {self.resident.name}"
