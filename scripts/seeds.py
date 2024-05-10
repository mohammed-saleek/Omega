from userprofile.models import (
    Profile, EducationDetails, ProfessionDetails, Address
)
edu = EducationDetails.objects.create(
    name="Bachelor of Computer Application", graduation_year=2018
)
edu.save()

prof = ProfessionDetails.objects.create(
    name="Software Programmer", company_name="ABC"
)
prof.save()