from rest_framework import serializers
from .models import * 

class LoyaltySerializer(serializers.ModelSerializer):
    class Meta:
        model=Loyalty
        fields='__all__'


LOYALTY_TIERS=(
    ('BRONZE','bronze'),
    ('SILVER','silver'),
    ('GOLD','gold'),
    ('PLATINUM','platinum'),
    ('DIAMOND','diamond'),
)
class LoyaltyProfileSerializer(serializers.ModelSerializer):
    loyalty_tier = serializers.ChoiceField(choices=LOYALTY_TIERS)
    class Meta:
        model=LoyaltyProfile
        fields='__all__'

     