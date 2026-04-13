from django.contrib import admin
from web.models import Profile, SocialLinks, Education, Experience, Skills, Technologies

# Register your models here.

admin.site.register(Profile)
admin.site.register(SocialLinks)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skills)
admin.site.register(Technologies)
