from django.db import models

# Create your models here.


class Session(models.Model):
    year = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return "Year: " + str(self.year)

class Bill(models.Model):
    bill_pk = models.CharField(max_length=100, primary_key=True)
    bill_number = models.CharField(max_length=100, null=False)
    bill_title = models.CharField(max_length=100, null=False)
    chamber_intro = models.CharField(max_length=100, null=False)
    summary = models.TextField(null=False)
    chief_patron = models.CharField(max_length=100, null=False)
    district = models.CharField(max_length=100,null=False)
    house_patrons = models.TextField(null=False)
    senate_patrons = models.TextField(blank=True)
    fulltext_i = models.TextField(blank=True)
    fulltext_p = models.TextField(blank=True)
    session = models.ForeignKey(Session, max_length=100, on_delete=models.CASCADE)



    def __str__(self):
        return str(self.session)+ " Bill Number: " + str(self.bill_number)
