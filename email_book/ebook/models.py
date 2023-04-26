from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(max_length=254,blank=False,null=False)
    company_name = models.EmailField(max_length=254,blank=False,null=False)
    company_website = models.CharField(max_length=100,blank=False,null=False)
    company_address = models.CharField(max_length=100,blank=False,null=False)
    city = models.CharField(max_length=50,blank=False,null=False)
    state = models.CharField(max_length=50,blank=False,null=False)
    zip_code = models.IntegerField(blank=False, null=False)
    country = models.CharField(max_length=10, blank=False)

# class (models.Model):
#     id = models.IntegerField(blank=False, null=False)
#     name = models.CharField(max_length=50,blank=True,null=True)
#     from_email = models.EmailField(max_length=254,blank=False,null=False)
#     to_email = models.EmailField(max_length=254,blank=False,null=False)
#     company_website = models.CharField(max_length=100,blank=False,null=False)
#     company_address = models.CharField(max_length=100,blank=False,null=False)
#     city = models.CharField(max_length=50,blank=False,null=False)
#     state = models.CharField(max_length=50,blank=False,null=False)
#     zip_code = models.IntegerField(max_length=10,blank=False,null=False)
#     country = models.CharField(max_length=10,blank=False,null=False)