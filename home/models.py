from django.db import models

# Create your models here.
# Database -------->Exel workbook
# Models in django --------> Table ---------->Sheet

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=15)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True ,blank=True)

    def __str__(self):
        return 'Message from ->' + self.name + ' -- '+ self.email