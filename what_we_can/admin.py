from django.contrib import admin
from .models import Health,Education,Environment,SocialCare

admin.site.register(Health)
admin.site.register(Education)
admin.site.register(Environment)
admin.site.register(SocialCare)