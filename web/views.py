from django.shortcuts import render
from web import models

# Create your views here.

def profile(request, id):
    profile_ = models.Profile.objects.get(id=id)
    links = models.SocialLinks.objects.filter(profiles_id=id)
    educations = models.Education.objects.filter(profiles_id=id)
    experiences = models.Experience.objects.filter(profiles_id=id)
    skills = models.Skills.objects.filter(profiles_id=id)
    contact = models.Contacts.objects.get(profiles_id=id)
    information = models.Information.objects.filter(profiles_id=id)

    return render(request, 'profile.html', {
        'profile':profile_,
        'links':links,
        'educations':educations,
        'experiences':experiences,
        'skills':skills,
        'contact':contact,
        'information':information
    })
