from django.core.management.base import BaseCommand
from django.utils import timezone

from backend.appointments.models import Appointment
from backend.notifications.models import EmergencyNotification
from backend.residents.models import Resident
from backend.visits.models import VisitRecord


class Command(BaseCommand):
    help = "Load demo data for local development."

    def handle(self, *args, **options):
        resident, _ = Resident.objects.get_or_create(
            name="李建国",
            room_number="A-302",
            defaults={
                "gender": "male",
                "age": 82,
                "care_level": "assisted",
                "emergency_contact": "李女士",
                "emergency_phone": "13800000001",
                "medical_notes": "高血压，需低盐饮食。",
            },
        )
        appointment, _ = Appointment.objects.get_or_create(
            resident=resident,
            family_name="李女士",
            visit_time=timezone.now() + timezone.timedelta(days=1),
            defaults={
                "family_phone": "13800000001",
                "relationship": "女儿",
                "visitor_count": 2,
                "status": "approved",
                "notes": "携带换季衣物。",
            },
        )
        VisitRecord.objects.get_or_create(
            appointment=appointment,
            defaults={
                "check_in_time": timezone.now() - timezone.timedelta(days=3),
                "check_out_time": timezone.now() - timezone.timedelta(days=3) + timezone.timedelta(hours=1),
                "visitor_temperature": "36.5",
                "staff_name": "王护士",
                "summary": "探视过程正常，老人精神状态良好。",
            },
        )
        EmergencyNotification.objects.get_or_create(
            title="端午假期探视安排",
            defaults={
                "content": "假期探视需提前一天预约，请家属配合体温登记。",
                "level": "warning",
                "target_group": "families",
                "is_active": True,
            },
        )
        self.stdout.write(self.style.SUCCESS("Demo data loaded."))
