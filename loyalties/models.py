from django.db import models
from users.models import *


LOYALTY_TYPES=(
    ('LOGIN','login'),
    ('REFERRAL','referral'),
    ('PURCHASE','purchase'),
    ('REVIEW','review'),

)

LOYALTY_TIERS=(
    ('BRONZE','bronze'),
    ('SILVER','silver'),
    ('GOLD','gold'),
    ('PLATINUM','platinum'),
    ('DIAMOND','diamond'),
)

class Loyalty(models.Model):
    type= models.CharField(choices=LOYALTY_TYPES, max_length=100)
    points= models.PositiveIntegerField(default=0)

    def __str__ (self):
        return str(self.type)


class LoyaltyToken(models.Model):
    monetary_value=models.PositiveIntegerField(null=True, blank=True)

class TierProgression(models.Model):
    name = models.CharField(max_length=100,choices=LOYALTY_TIERS)
    order = models.PositiveIntegerField(unique=True)
    minimum_points = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name    


class LoyaltyProfile(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    loyalty_tier = models.ForeignKey(TierProgression, on_delete=models.PROTECT,default=1,null=True, blank=True)
    current_points=models.PositiveIntegerField( default=0)
    maximum_points=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.customer.user.email
    
    def calculate_current_tier(self):
        tiers = TierProgression.objects.filter(minimum_points__lte=self.current_points)
        latest_tier = tiers.order_by('-order').first()
        if latest_tier:
            self.loyalty_tier = latest_tier
            self.save()

