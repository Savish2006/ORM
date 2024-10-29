from django.db import models
from django.contrib import admin
class Bankloan (models.Model):
   name=models.CharField(max_length=20)
   acc_no=models.CharField(max_length=20,primary_key=True)
   age=models.IntegerField()
   amount=models.IntegerField()
   ifsc_code=models.IntegerField()
   

class BankloanAdmin(admin.ModelAdmin):
 list_display=('name','acc_no','age','amount','ifsc_code')

