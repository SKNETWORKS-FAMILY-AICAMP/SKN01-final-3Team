from django.db import models

from account.entity.account import Account

class Profile(models.Model):
    email = models.CharField(max_length=64, unique=True)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f"Profile -> email: {self.email}"

    class Meta:
        db_table = 'profile'
        app_label = 'account'
