from rest_framework import serializers

from .models import Ticket


class TicketSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=40)
    address = serializers.CharField()
    mobileNo = serializers.CharField(max_length=10)
    email = serializers.EmailField()
    dob = serializers.DateField()
    from_station = serializers.CharField(max_length=40)
    to_station = serializers.CharField(max_length=40)
    doj = serializers.DateField()
    ticket_no = serializers.CharField(max_length=8)
    train_no = serializers.CharField(max_length=5)
    train_name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Ticket.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # whatever fields you put here, during PUT operation you have to enter all those fields.
        # If you don't write this function you needn't give all fields

        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.mobileNo = validated_data.get('mobileNo', instance.mobileNo)
        instance.email = validated_data.get('email', instance.email)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.from_station = validated_data.get('from_station', instance.from_station)
        instance.to_station = validated_data.get('to_station', instance.to_station)
        instance.doj = validated_data.get('doj', instance.doj)
        instance.ticket_no = validated_data.get('ticket_no', instance.ticket_no)
        instance.train_no = validated_data.get('train_no', instance.train_no)
        instance.train_name = validated_data.get('train_name', instance.train_name)

        instance.save()
        return instance
