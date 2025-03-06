from django.db import models

class BankAccount(models.Model):
    username = models.CharField(max_length=20)
    account_number = models.CharField(max_length=16, unique=True)
    Emailid= models.EmailField(max_length=20)

   

class Transaction(models.Model):
    sender = models.ForeignKey(BankAccount, related_name='sent_transactions', on_delete=models.CASCADE)
    receiver = models.ForeignKey(BankAccount, related_name='received_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Completed')

   
