from rest_framework import serializers
from django.contrib.auth.models import User
from Acme_Support.models import Ticket, Category


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff')


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id','title', 'ticket_id','user','status','content', 'category','created', 'modified')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name', 'slug')
