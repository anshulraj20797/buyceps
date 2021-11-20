from django.db import models

OPERATION_CHOICE = (('reverse','reverse'),('reverse_word ','reverse_word'),('flip','flip'),('sort','sort'))
class Detail(models.Model):
    id_no = models.BigAutoField(auto_created=True, primary_key=True)
    text = models.TextField()

    def __str__(self):
        return self.id_no

class Transaction(models.Model):
    id_no = models.BigIntegerField()
    operation = models.CharField(max_length=200, choices=OPERATION_CHOICE)
    new_text = models.TextField()

    def __str__(self):
        return self.id_no


