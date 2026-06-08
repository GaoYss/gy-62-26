from django.db import models


class EmergencyNotification(models.Model):
    LEVEL_CHOICES = [
        ("info", "普通"),
        ("warning", "重要"),
        ("critical", "紧急"),
    ]

    TARGET_CHOICES = [
        ("all", "全部"),
        ("families", "家属"),
        ("staff", "员工"),
    ]

    title = models.CharField("标题", max_length=100)
    content = models.TextField("内容")
    level = models.CharField("级别", max_length=20, choices=LEVEL_CHOICES, default="warning")
    target_group = models.CharField("通知对象", max_length=20, choices=TARGET_CHOICES, default="families")
    is_active = models.BooleanField("是否有效", default=True)
    published_at = models.DateTimeField("发布时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title
