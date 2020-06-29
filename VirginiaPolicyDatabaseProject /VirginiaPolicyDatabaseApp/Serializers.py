from rest_framework import serializers

from .models import Bill, Session

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"
    def create(self, validated_data):
        return Bill.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.bill_number = validated_data.get('bill_number', instance.bill_number)
        instance.bill_title = validated_data.get('bill_title', instance.bill_title)
        instance.chamber_intro = validated_data.get('chamber_intro', instance.chamber_intro)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.chief_patron = validated_data.get('chief_patron', instance.chief_patron)
        instance.district = validated_data.get('district', instance.district)
        instance.house_patrons = validated_data.get('house_patrons', instance.house_patrons)
        instance.senate_patrons = validated_data.get('senate_patrons', instance.senate_patrons)
        instance.fulltext_i = validated_data.get('fulltext_i', instance.fulltext_i)
        instance.fulltext_p = validated_data.get('fulltext_p', instance.fulltext_p)
        instance.session = validated_data.get('session', instance.session)
        instance.save()
        return instance

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"

    def create(self, validated_data):
        return Session.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.year = validated_data.get('year', instance.year)
        instance.save()
        return instance

