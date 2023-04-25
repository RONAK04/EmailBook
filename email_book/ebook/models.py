from django.db import models

STATE_CHOICES = (
    ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Dadra Nagar Haveli','Dadra Nagar Haveli'),
    ('Diu Daman','Diu Daman'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu & Kashmir','Jammu & Kashmir'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Lakshadweep','Lakshadweep'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Puducherry','Puducherry'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttarakhand','Uttarakhand'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('West Bengal','West Bengal')
)

COUNTRY_CHOICES = (
    
)

class sender(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=50,blank=True,null=True)
    from_email = models.EmailField(max_length=254,blank=False,null=False)
    to_email = models.EmailField(max_length=254,blank=False,null=False)
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