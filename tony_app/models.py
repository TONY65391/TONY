from django.db import models

class JSS1(models.Model):
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Age = models.IntegerField(null = True)
    Fathers_Phone_Number = models.IntegerField(null = True)
    Mothers_Phone_Number = models.IntegerField(null = True)
    Address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"

class JSS2(models.Model):
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Age = models.IntegerField(null = True)
    Fathers_Phone_Number = models.IntegerField(null = True)
    Mothers_Phone_Number = models.IntegerField(null = True)
    Address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"
    
class JSS3(models.Model):
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Age = models.IntegerField(null = True)
    Fathers_Phone_Number = models.IntegerField(null = True)
    Mothers_Phone_Number = models.IntegerField(null = True)
    Address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"