from django.db import models

class Transaction(models.Model):
    id=models.AutoField(primary_key=True)
    customer=models.ForeignKey('users.Customer',on_delete=models.CASCADE)
    amount=models.FloatField()
    date=models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        db_table='transactions'
    def __str__(self):
        return str(self.id)
