from django.db.models import query
from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Detail, Transaction
from .serializers import DetailSerializer,TransactionSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404



class DetailViewSet(viewsets.ModelViewSet):
    serializer_class = DetailSerializer
    queryset = Detail.objects.all()

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    def retrieve(self, request, pk):
        transaction = Transaction.objects.filter(id_no=pk)
        serializer = self.serializer_class(transaction, many=True)
        return Response(serializer.data)