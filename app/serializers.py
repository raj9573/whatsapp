from rest_framework import serializers

from app.models import *
from django.utils.timesince import timesince
from datetime import datetime

def format_time_difference(created_on):
    now = timezone.now()
    delta = now - created_on

    # Convert timedelta to human-readable format
    if delta.days > 7:
        weeks = delta.days // 7
        return f"{weeks} {'week' if weeks == 1 else 'weeks'} ago"
    elif delta.days > 0:
        return f"{delta.days} {'day' if delta.days == 1 else 'days'} ago"
    elif delta.seconds >= 3600:
        hours = delta.seconds // 3600
        return f"{hours} {'hour' if hours == 1 else 'hours'} ago"
    elif delta.seconds >= 60:
        minutes = delta.seconds // 60
        return f"{minutes} {'minute' if minutes == 1 else 'minutes'} ago"
    else:
        return "Just now"

class userserializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'


class friendsserializer(serializers.ModelSerializer):
    friend = userserializer()
    class Meta:
        model = friends
        fields = ['friend']


class messagesserializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    # receiver = userserializer()
    def get_created_at(self, obj):
        return format_time_difference(obj.created_at)
    class Meta:
        model = messages

        fields = '__all__'
        