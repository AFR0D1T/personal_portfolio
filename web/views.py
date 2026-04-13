from django.shortcuts import render
from web import models

# Create your views here.

def profile(request, id):
    profile_ = models.Profile.objects.get(id=id)
    links = models.SocialLinks.objects.filter(profiles_id=id)
    educations = models.Education.objects.filter(profiles_id=id)
    experience = models.Experience.objects.filter(profiles_id=id)
    skills = models.Skills.objects.filter(profiles_id=id)
    contact = models.Contacts.objects.get(profiles_id=id)

    return render(request, 'profile.html', {
        'profile':profile_,
        'links':links,
        'educations':educations,
        'experience':experience,
        'skills':skills,
        'contact':contact
    })
