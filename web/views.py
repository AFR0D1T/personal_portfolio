from django.shortcuts import render
from web import models

# Create your views here.

def profile(request, id):
    profile_ = models.Profile.objects.get(id=id)
    links = models.SocialLinks.objects.filter(profiles_id=id)
    education = models.Education.objects.filter(profiles_id=id)
    experience = models.Experience.objects.filter(profiles_id=id)
    skills = models.Skills.objects.filter(profiles_id=id)

    return render(request, 'profile.html', {
        'profile':profile_,
        'links':links,
        'education':education,
        'experience':experience,
        'skills':skills
    })
