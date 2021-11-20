from django.db import models
from django.db.models import fields
from rest_framework.fields import IntegerField
from rest_framework.relations import ManyRelatedField
from rest_framework.utils import field_mapping
from .models import Detail, Transaction
from rest_framework import serializers
import datetime


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ['id_no','text']

 
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id_no','operation','new_text']
        extra_kwargs = {
            'new_text' : {
                'read_only': True,
            }
        }

    def string_manipulation(self, id_no):
        text = Detail.objects.get(id_no=id_no)
        now = datetime.datetime.now()
        tn = now.strftime("%H%M")
        modified_string = text.text + '/' + str(tn)
        return modified_string

    def create(self, validated_data):
        modified_string = self.string_manipulation(validated_data['id_no'])
        transaction = Transaction(
            id_no=validated_data['id_no'],
            operation=validated_data['operation'],
            new_text=modified_string
            )
        transaction.save()
        original_text = Detail.objects.get(id_no=validated_data['id_no'])
        original_text.text = modified_string
        original_text.save()

        return transaction

