from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Loyalty)
admin.site.register(LoyaltyProfile)
admin.site.register(LoyaltyToken)
admin.site.register(TierProgression)

