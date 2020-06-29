from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .Serializers import BillSerializer, SessionSerializer
from .models import Bill, Session



class SessionViewSet(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    queryset = Session.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = SessionSerializer(data = request.data)
        if serializer.is_valid():
            session = serializer.save()
            return Response(SessionSerializer(session).data)
        else:
            return Response({"message":"Could not create the Session"})

    def retrieve(self, request, *args, **kwargs):
        session = Session.objects.get(year = kwargs["pk"])
        serializer = SessionSerializer(session)
        return Response(serializer.data)



class BillViewSet(viewsets.ModelViewSet):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = BillSerializer(data = request.data)
        if serializer.is_valid():
            bill = serializer.save()
            return Response(BillSerializer(bill).data)
        else:
            return Response({"message":"Could not create the Bill"})

    def list(self, request, *args, **kwargs):
        if 'year' in kwargs:
            bill = Bill.objects.filter(session = Session.objects.get(year = kwargs["year"]))
            serializer = BillSerializer(bill, many=True)

            if 'bill_number' in kwargs:
                bill = bill.get(year = kwargs["bill_number"])
                serializer = BillSerializer(bill)
            return Response(serializer.data)
        else:
            return super().list(request, *args, **kwargs)

    '''
    def update(self, request, pk, *args, **kwargs):

        bill = Bill.objects.get(bill_number=pk)
        print("Bill updated = " + bill.bill_number)
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            pk = validated_data.get("created_by")
            bill.bill_number = validated_data.get("bill_number")
            bill.bill_title = validated_data.get("bill_title")
            bill.chamber_intro = validated_data.get("chamber_intro")
            bill.summary = validated_data.get("summary")
            bill.chief_patron = validated_data.get("chief_patron")
            bill.district = validated_data.get("district")
            bill.house_patrons = validated_data.get("house_patrons")
            bill.senate_patrons = validated_data.get("senate_patrons")
            bill.session = validated_data.get("session")
            bill.save()
        return Response(BillSerializer(bill).data)
    '''


