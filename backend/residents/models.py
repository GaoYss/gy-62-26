from django.db import models


class Resident(models.Model):
    GENDER_CHOICES = [
        ("male", "男"),
        ("female", "女"),
    ]

    CARE_LEVEL_CHOICES = [
        ("self_care", "自理"),
        ("assisted", "介助"),
        ("nursing", "介护"),
    ]

    name = models.CharField("姓名", max_length=50)
    gender = models.CharField("性别", max_length=10, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField("年龄")
    room_number = models.CharField("房间号", max_length=20)
    care_level = models.CharField("护理等级", max_length=20, choices=CARE_LEVEL_CHOICES)
    emergency_contact = models.CharField("紧急联系人", max_length=50)
    emergency_phone = models.CharField("紧急联系电话", max_length=30)
    medical_notes = models.TextField("健康备注", blank=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        ordering = ["room_number", "name"]

    def __str__(self):
        return f"{self.name}({self.room_number})"
