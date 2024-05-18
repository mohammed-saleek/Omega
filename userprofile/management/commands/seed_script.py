from django.core.management.base import BaseCommand
from userprofile.models import (
    Profile, EducationDetails, ProfessionDetails, Address
)


class Command(BaseCommand):
    help = 'Inserts data into the db'

    def handle(self, *args, **kwargs):
        edu = EducationDetails.objects.create(
            name="Bachelor of Computer Science", graduation_year=2018
        )
        edu.save()

        prof = ProfessionDetails.objects.create(
            name="Software Developer", company_name="ZIL"
        )
        prof.save()
        return "success"